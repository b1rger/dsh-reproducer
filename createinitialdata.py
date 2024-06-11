from foobar.models import Profession, Person

pro = Profession.objects.create()
p = Person.objects.create()
p.profession.add(pro)
