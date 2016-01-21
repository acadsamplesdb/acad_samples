import argparse
import xlrd
import json
import string


class ReadFromExcel(object):
    """
    Read data from Excel source and return a JSON representation suitable for
    passing to Django's serializers.deserialize()

    Also has some hacks/normalisations specific to ACAD samples database source data
    """
    def __init__(self, input, prefix='samples'):
        self.wb = xlrd.open_workbook(file_contents=input)
        self.prefix = prefix

    def _read_from_sheet(self, sheet):
        model = self.prefix + '.' + sheet.name.lower()
        processed_sheet = []

        for row in range(1, sheet.nrows):
            fields = {}
            date_notes = []

            for col in range(0, sheet.ncols):
                cell_type = sheet.cell_type(row, col)
                cell_value = sheet.cell_value(row, col)
                cell_header = sheet.cell_value(0, col)

                if cell_type == xlrd.XL_CELL_DATE:
                    date_tuple = xlrd.xldate_as_tuple(cell_value, sheet.book.datemode)
                    value = "%04i-%02i-%02i" % (date_tuple[0], date_tuple[1], date_tuple[2])

                elif cell_type == xlrd.XL_CELL_NUMBER:
                    num = float(cell_value)
                    if num.is_integer():
                        value = int(num)
                    else:
                        value = num

                else:
                    value = str(cell_value).strip()

                if sheet.name.lower() == "sample":
                    if cell_header == "group" and value != "":
                        """ Skip values that aren't actually GPxxx numbers """
                        if value.lower() in ["na", "n/a", "excontr", "tba"]:
                            continue
                        value = str(value).lstrip("GP")
                        import re
                        value = re.sub(r"^0+", "", value)
                        # If there's nothing numeric remaining, prepend a zero.
                        # No, this isn't going to win any prizes for elegance.
                        if value == "" or value[0] not in string.digits:
                            value = "0" + value

                """ Workaround for date fields without full year-month-day dates """
                if sheet.name.lower() == "sample":
                    if cell_header == "collection_date" and value != "":
                        if cell_type != xlrd.XL_CELL_DATE:
                            date_notes.append("Collection date: {}".format(value))
                            value = ""
                if sheet.name.lower() == "sample":
                    if cell_header == "sample_date" and value != "":
                        if cell_type != xlrd.XL_CELL_DATE:
                            date_notes.append("Sample date: {}".format(value))
                            value = ""

                if sheet.name.lower() == "aqissamplegroup":
                    if cell_header == "group_num" and value != "":
                        value = str(value).lstrip("GP")
                        try:
                            value = int(value)
                        except ValueError:
                            """ Ok, it's not an integer -- strip leading zeroes """
                            import re
                            value = re.sub(r"^0+", "", value)

                if value != "":
                    field = cell_header.strip()
                    fields[field] = value
                if date_notes:
                    fields["date_notes"] = (". ").join(date_notes)

            """ Concatenate the various note-type fields into 'notes' """
            if sheet.name.lower() == "sample":
                note_elems = []
                for note_field in ["description", "notes", "details", "collection_details", "collection_notes", "other_notes", "date_notes"]:
                    if note_field in fields:
                        note_elems.append(str(fields.get(note_field, None)))
                        del fields[note_field]
                fields["notes"] = (". ").join(filter(None, note_elems))

            for pkfield in ["acad_num", "group_num"]:
                if pkfield in fields:
                    pk = fields.pop(pkfield)
                    break
                else:
                    pk = ""

            dict = {'fields': fields, 'model': model}
            if pk != "":
                dict["pk"] = pk
            processed_sheet.append(dict)

        return processed_sheet

    def json_from_sheets(self):
        data = []

        for sheet in self.wb.sheets():
            """ If sheet name starts with '_', skip processing that sheet """
            if sheet.name[0] == "_":
                continue
            data.extend(self._read_from_sheet(sheet))

        jsondata = json.dumps(data, indent=2)
        return jsondata

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('infilename', help='Excel source file')
    args = parser.parse_args()

    with open(args.infilename, 'rb') as infile:
        excel = ReadFromExcel(infile.read())
        print(excel.json_from_sheets())
