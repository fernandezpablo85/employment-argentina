provinces = ['CABA', 'Buenos Aires', 'Catamarca', 'Cordoba', 'Corrientes', 'Chaco', 'Chubut',
  'Entre Rios', 'Formosa', 'Jujuy', 'La Pampa', 'La Rioja', 'Mendoza', 'Misiones', 'Neuquen',
  'Rio Negro', 'Salta', 'San Juan', 'San Luis', 'Santa Cruz', 'Santa Fe', 'Santiago del Estero',
  'Tierra del Fuego', 'Tucuman', 'NA']

quarters = ['Q1-04', 'Q2-04', 'Q3-04', 'Q4-04', '04', 'Q1-05', 'Q2-05', 'Q3-05', 'Q4-05', '05',
  'Q1-06', 'Q2-06', 'Q3-06', 'Q4-06', '06', 'Q1-07', 'Q2-07', 'Q3-07', 'Q4-07', '07', 'Q1-08',
  'Q2-08', 'Q3-08', 'Q4-08', '08', 'Q1-09', 'Q2-09', 'Q3-09', 'Q4-09', '09', 'Q1-10', 'Q2-10',
  'Q3-10', 'Q4-10', '10', 'Q1-11', 'Q2-11', 'Q3-11', 'Q4-11', '11', 'Q1-12', 'Q2-12', 'Q3-12',
  'Q4-12', '12', 'Q1-13', 'Q2-13', 'Q3-13', 'Q4-13', '13', 'Q1-14', 'Q2-14', 'Q3-14', 'Q4-14', '14',
  'Q1-15', 'Q2-15', 'Q3-15', 'Q4-15', '15', 'Q1-16', 'Q2-16']

def remove_thousands_separator(lines):
  """Remove thousands separator.
  e.g. 1,000,00 becomes 1000000
  """
  return map(lambda s: s.replace(',', '').rstrip() , lines)

def is_quarter(string):
  """Determine if measurement label is quarterly."""
  return string.startswith('Q')

def format_csv(entry):
  """Format a data entry as a csv line."""
  return "%s, %s, %s" % (entry['province'], entry['quarter'], entry['count'])

def format_json(entry):
  """Format a data entry as a json object."""
  return '{ "province": "%s", "quarter": "%s", "count": "%s" }' % (entry['province'], entry['quarter'], entry['count'])

def create_data_structure(lines):
  """Add province and quarter data to measurements."""
  data = []
  for i, line in enumerate(lines):
    province = provinces[i]
    measures = line.split()
    for j, m in enumerate(measures):
      quarter = quarters[j]

      # avoid year means.
      if not is_quarter(quarter): continue
      data.append({'province': province, 'quarter': quarter, 'count': m})
  return data

import sys

# check if we have standard input.
if sys.stdin.isatty():
  print "usage: cleanup_provinces.py < [input.txt]"
  exit(1)

lines = sys.stdin.readlines()
no_separator = remove_thousands_separator(lines)
data = create_data_structure(no_separator)

csv = map(format_csv, data)
for item in csv:
  print item
