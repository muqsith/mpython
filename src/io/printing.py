
year = 2016
event = 'Referendum'
s = f'Results of the {year} {event}'

print(s)

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-10} YES votes  {:2.4%}'.format(yes_votes, percentage))