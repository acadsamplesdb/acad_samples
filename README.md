ACAD samples database

##Requirements and rules

0. A normal user should not be able to delete a sample if the sample has associated children e.g. extractions, amplifications. Only an administrator would be able to delete a sample and all its’ associations.
0. The rules when using *Upload samples* when the ‘Group’ column is either blank or has a GP number.

    0. Scenario: ‘Group’ is blank or contains a number that is not prefixed by GP. Rules to apply:
          0. ‘Group’ remains blank if “Make a new AQIS group from these samples?” is unchecked.
          0. Next available GP number is created and the sample is assigned to new group if “Make a new AQIS group from these samples?” is checked.
    0. Scenario: ‘Group’ contains a number that is prefixed by GP. Rules to apply:
          0. If GP number already exists then sample is assigned to existing group
          0. If GP number does not exist then new group is created using the GP number entered. The sample will be assigned to this new group.

    In both the above cases, the check or unchecked selection on “Make a new AQIS group from these samples?” will be ignored. However, inform user that the selection was ignored for samples that have GP numbers entered in the Group column
