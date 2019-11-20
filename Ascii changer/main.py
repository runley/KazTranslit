#---------------------------------------
#main
#---------------------------------------
#imports go here
import functions as fn
import os
#---------------------------------------
#dictionary with definitions of the char.
kazalphabet = {"\u0410":"A","\u04d8":"\u00c4","\u0411":"B","\u0412":"V","\u0413":"G","\u0492":"\u011e","\u0414":"D","\u0415":"E","\u0401":"YO","\u0416":"J","\u0417":"Z","\u0418":"\u00cf","\u0419":"Y","\u041a":"K","\u049a":"Q","\u041b":"L","\u041c":"M","\u041d":"N","\u04a2":"\u00d1","\u041e":"O","\u04e8":"\u00d6","\u041f":"P","\u0420":"R","\u0421":"S","\u0422":"T","\u0423":"W","\u04b0":"U","\u04ae":"\u00dc","\u0424":"F","\u0425":"X","\u04ba":"H","\u0426":"C","\u0427":"\u00c7","\u0428":"\u015e","\u0429":"\u015e\u00c7","\u042a":"\"","\u042b":"I","\u0406":"I","\u042c":"\'","\u042d":"\u00c9","\u042e":"YU","\u042f":"YA","\u0430":"a","\u04d9":"\u00e4","\u0431":"b","\u0432":"v","\u0433":"g","\u0493":"\u011f","\u0434":"d","\u0435":"e","\u0451":"yo","\u0436":"j","\u0437":"z","\u0438":"\u00ef","\u0439":"y","\u043a":"k","\u043b":"l","\u043c":"m","\u043d":"n","\u04a3":"\u00f1","\u043e":"o","\u04e9":"\u00f6","\u043f":"p","\u0440":"r","\u0441":"s","\u0442":"t","\u0443":"w","\u04b1":"u","\u04af":"\u00fc","\u0444":"f","\u0445":"x","\u04bb":"h","\u0446":"c","\u0447":"\u00e7","\u0448":"\u015f","\u0449":"\u015f\u00e7","\u044a":"\"","\u044b":"\u0131","\u0456":"i","\u044c":"\'","\u044d":"\u00e9","\u044e":"yu","\u044f":"ya"}
#---------------------------------------
#vars for initilisation
count = 0
Buffer = "buffer.txt"
userInput = fn.userInput()
userFile = fn.askUser(userInput)
#---------------------------------------
#clean buffer
fn.bufferCleaner(Buffer)
#---------------------------------------
#program code
if os.path.exists(userInput):
  for line in userFile:
    fn.StringChanger(line,Buffer,kazalphabet)
    #print("line {0} completed successfully.".format(count))
    count += 1
  print("all lines completed.")
  input("press 'enter' to leave\n>>>")
else:
  print("path does not exist.")
#---------------------------------------
#NOTES TO SELF
#
