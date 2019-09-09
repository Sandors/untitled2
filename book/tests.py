from django.test import TestCase

# Create your tests here.
print('\n'.join([''.join([('love'[(a-b) % len('Love')]
                           if ((a*0.05)**2+(b*0.1)**2-1)**3-(a*0.05)**2*(b*0.1)**3 <= 0 else ' ')
                          for a in range(-30, 30)])
                 for b in range(30, -30, -1)]))