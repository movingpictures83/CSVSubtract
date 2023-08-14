import PyIO
import PyPluMA

class CSVSubtractPlugin:
    def input(self, inputfile):
       self.parameters = PyIO.readParameters(inputfile)

    def run(self):
       pass

    def output(self, outputfile):
       csv1 = open(PyPluMA.prefix()+"/"+self.parameters["csv1"], 'r')
       csv2 = open(PyPluMA.prefix()+"/"+self.parameters["csv2"], 'r')
       csvout = open(outputfile, 'w')
       csvout.write(csv1.readline())
       csv2.readline()
       for line1 in csv1:
           contents1 = line1.strip().split(',')
           contents2 = csv2.readline().strip().split(',')
           csvout.write(contents1[0])
           csvout.write(',')
           for i in range(1, len(contents1)):
              csvout.write(str(float(contents1[i])-float(contents2[i])))
              if (i != len(contents1)-1):
                  csvout.write(',')
              else:
                  csvout.write('\n')

