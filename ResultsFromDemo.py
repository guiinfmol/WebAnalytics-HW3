import src.Beam as Beam
import csv
import src.Functions as f

'''


Traffic Source = direct_traffic , quality = 0.0637160481082224
Screen Resolution = Extra Small ^ Traffic Source = direct_traffic, quality = 0.06339326301193321
Browser = Chrome Mobile ^ Traffic Source = direct_traffic, quality = 0.0627037172080491
OS = Android ^ Traffic Source = direct_traffic, quality = 0.06567103001403078
Traffic Source = direct_traffic ^ User Language = en-us, quality = 0.06157116948587219

'''
eq = Beam.eq

file = open('data/finalDataset.csv', encoding='latin-1')
a = csv.reader(file, dialect='excel-tab')

# A little bit of processing of the data. Make data a list as well as removing rows with missing attributes.
data =[]

for i in a:
    data.append(i)

ref_length = len(data[0])

print("Analysing ", len(data[1:]), " rows.")

# All features used in the example are nominal, except for returning visitor that is going to be binary (0/1-represented)
names = data[0]
ind_of = names.index('Returning Visitor')

types = ['nominal' for _ in range(0, len(data[0]))]
types[ind_of] = 'binary'

traff_ind = names.index('Traffic Source')
screen_ind = names.index('Screen Resolution')
browser_ind = names.index('Browser')
os_ind = names.index('OS')
usrlang = names.index('User Language')

#Description & Subgroup 1
desc1 = ((traff_ind, 'direct_traffic', eq), )
subgroup1 = Beam.get_subgroup(desc1, data)

#Description & Subgroup 2
desc1 = ((screen_ind, 'Extra Small', eq), (traff_ind, 'direct_traffic', eq))
subgroup2 = Beam.get_subgroup(desc1, data)

#Description & Subgroup 3
desc1 = ((browser_ind, 'Chrome Mobile', eq), (traff_ind, 'direct_traffic', eq))
subgroup3 = Beam.get_subgroup(desc1, data)

#Description & Subgroup 4
desc1 = ((os_ind, 'Android', eq), (traff_ind, 'direct_traffic', eq))
subgroup4 = Beam.get_subgroup(desc1, data)

#Description & Subgroup 5
desc1 = ((usrlang, 'en-us', eq), (traff_ind, 'direct_traffic', eq))
subgroup5 = Beam.get_subgroup(desc1, data)

yuleQ = f.yuleQ(data,[4,5], data)

print(yuleQ)

print("Subgroup 1", len(subgroup1))
f.yuleQualityMeasure(data, subgroup1, [4,5])
print("Subgroup 2", len(subgroup2))
f.yuleQualityMeasure(data, subgroup2, [4,5])
print("Subgroup 3", len(subgroup3))
f.yuleQualityMeasure(data, subgroup3, [4,5])
print("Subgroup 4", len(subgroup4))
f.yuleQualityMeasure(data, subgroup4, [4,5])
print("Subgroup 5", len(subgroup5))
f.yuleQualityMeasure(data, subgroup5, [4,5])


