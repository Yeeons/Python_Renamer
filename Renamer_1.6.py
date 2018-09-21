### Dependencies 
# Howbrew - copy and paste in the line below
"""/usr/bin/ruby -e '$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)' """

# Pip - copy and paste in the line below
"""curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py"""
"""python get-pip.py --user """

# Pdftotext - copy and paste in the line below
"""sudo pip install pdftotext"""


# pdftotext required to work
import pdftotext
import re
import os 

#finds the current directory
directory = os.path.dirname(os.path.realpath(__file__))


#Checks to see if the file name exists before

## Notworking properly needs a save instead of a rename
def check_and_rename(file, filename, add = 0):
    orginal_name = file
    if add != 0:
        split = file.split(".")
        part_1 = split[0] + "_" + str(add)
        file = ".".join([part1, split[1]])
    if not os.path.isfile(file):
        os.write(file, f)
    else:
        check_and_rename(orginal_name, add = add + 1)


for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
        
        with open(filename, "rb") as f:
            pdf = pdftotext.PDF(f)

            # Read all the text into one string
            complete_copy = ("\n\n".join(pdf))

            try:
                finder = re.search('[xA-Z0-9]+_[xA-Z0-9]+_[xA-Z0-9]+_[xA-Z0-9]+', complete_copy).group()

                finder_2 = len(re.findall('[xA-Z0-9]+_[xA-Z0-9]+_[xA-Z0-9]+_[xA-Z0-9]+',complete_copy))

                if finder_2 > 1:
                
                    finder_checker = re.findall('[xA-Z0-9]+_[xA-Z0-9]+_[xA-Z0-9]+_[xA-Z0-9]+', complete_copy)

                    if finder_checker[0] == finder_checker[1]:

                        finder_name = finder + ".pdf"

                        check_and_rename(finder_name, filename)

                        print(". " )

                    else: 
                        print("x " + str(finder_2) + "_" + finder_name + "---Key Numbers don't match")
                        os.rename(filename, "_No Matching Key Num_" + filename)


                else:
                    print("XXX " + str(finder_2) + filename + "---Key Numbers don't match" + str(finder))
                    os.rename(filename, "_No Matching Key Num_" + filename)


            except:
                print(filename + "---!!!Found nothing.")
                os.rename(filename, "_Failed_" + filename)
              
        continue
    else:
        continue

print("Complete")
