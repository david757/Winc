__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os 
import zipfile




def clean_cache():  
    if (os.path.exists('C:\\Users\\david\\Winc\\files\\cache')) == False:
        os.makedirs('cache')
    elif (os.path.exists('C:\\Users\\david\\Winc\\files\\cache')) == True:
            os.path.isdir('C:\\Users\\david\\Winc\\files\\cache') and os.path.getsize('C:\\Users\\david\\Winc\\files\\cache') > 0
            files_in_directory = os.listdir('C:\\Users\\david\\Winc\\files\\cache')
            filtered_files = [file for file in files_in_directory if file.endswith(".txt")]
            for file in filtered_files:
	            path_to_file = os.path.join(directory, file)
	            os.remove(path_to_file)
            return

def cache_zip():
    handle = zipfile.ZipFile('C:\\Users\\david\\Winc\\files\\data.zip')
    handle.extractall('C:\\Users\\david\\Winc\\files\\cache')
    handle.close()
    return

def cached_files():
    print(os.listdir('C:\\Users\\david\\Winc\\files\\cache'))
    return


def find_password():
    filenames = []

    for root, dirs, files in os.walk(r"C:\\Users\\david\\Winc\\files\\cache"):

        for filename in files:
            if(filename.endswith(".txt")):

                filenames.append(filename)
            
    for filename in filenames:
        file = open('C:\\Users\\david\\Winc\\files\\cache\\'+ filename,'r')
        for line in file:
            if("password") in line:
                print(line)
            else:
                pass
    print("\n")
    file.close()

find_password()

 









#if print(os.path.isdir('C:\\Users\\david\\Winc\\files\\cache') and os.path.getsize('C:\\Users\\david\\Winc\\files\\cache') == 0):
  #  os.makedirs(cache)

 
#path= 'C:\\Users\\david\\Winc\\files'
#os.chdir(path)
#newfolder = 'cache'
#os.makedirs(newfolder)

#print(os.path.isdir('C:\\Users\\david\\Winc\\files\\cache') and os.path.getsize('C:\\Users\\david\\Winc\\files\\cache'))

#1 map 'cache'aanmaken, als deze map er al is dan alles in de map verwijderen
#2 unzip in cache map
#3 lijst met alle bestanden in de map
#4 alle tekstfiles doorzoeken naar het "password" (601)