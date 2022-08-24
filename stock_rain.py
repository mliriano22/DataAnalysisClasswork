"""
    CS051P Lab Assignments: Stock v.s. Rain

    Author: Marilyn Liriano

    Date:  April 26, 2020

    The goal of this assignment is to familiarize you with data analysis
    and visualization. You'll practice handling files in csv format,
    create and manipulate Python dictionaries, and do some basic plotting
    using the matplotlib package.
"""
import matplotlib.pyplot as plt
import sys

#plt.plot([1,2,3,4,5], [20, 30, 10, 20, 0])
#plt.show()

def parse_rainfall(fname):
    """
    opens file and reads it to return a dictionary of dates as keys and weather data as values
    param fname: (string) name of file
    return rainfall: (dictionary) a dictionary of dates and their respective weather values
    """

    rainfall= {} #creates new empty dictionary
    count= 0
    with open(fname,'r') as f:
        for line in f:
            count= count+ 1
            if count > 1: #skips the header of the excel file that tells the categories
                set=line.split(",") #splits the line so you can access the different elements in the line
                if (set[1]) != ('"NA"'): #will create an entry for date with data
                    rainfall[line[1:11]] = float(set[1])
    return(rainfall)


def convertdate(date):
    """
    takes a date in the format m/d/year and converts it to year-month-day
    param date: (string) date in old format
    return newdate: (string) date in new format
    """
    date= date.split("/") #splits date by /
    if len(date[1]) == 1: #if the day is one number it puts a zero in front of it
        day= "0" + str(date[1])
    else:
        day = str(date[1])

    if len(date[0]) == 1:#if the month is one number it puts a zero in front of it
        month = "0" + str(date[0])
    else:
        month = str(date[0])

    newdate= "20" + str(date[2]) + "-" + month + "-" + day #adds strings to create dates
    return newdate

def parse_stock(fname, sym):
    # TODO:
    #  1. write the complete docstring of this function.
    #  2. implement this function as specified in the handout
    """
    opens file and reads it to return a dictionary of dates as keys and change in price as values
    param fname: (string) name of file
    param sym: (string) name of stock
    return: (dictionary) a dictionary of dates for a stock and their respective change in price
    if there is no change in price, an empty set is returned
    """
    pass
    stocks= {} #creates new empty dictionary
    count= 0

    with open(fname,'r') as f: #opens file
        for line in f:
            count = count + 1

            if count > 1: #skips the header of the excel file that tells the categories
                line.strip("\n")

                if line.strip("\n") == (""): #skips empty lines
                    pass

                else:
                    set = line.strip().split(",")
                    if set[4] != ("") and set[1] != ("") and set[6] == sym.strip("\n"):
                        #checks if there is change in price and if symbol matches

                        stocks[convertdate(set[0])] = float(((float(set[4]) - float(set[1]))))
                        # creates dictionary entries with date and change in price
        return stocks
        #returns dictionary of stocks



def correlate_data(stock_dict, rain_dict):
    """
    creates a nested list with values that are for common dates. each date will have its own list
    with values in the nested list
    param stock_dict: (dictionary) a dictionary of dates for a stock and their respective change in price
    param rain_dict: (dictionary)  a dictionary of dates and their respective weather values
    return: (list) a list of a list of values for a common date
    """
    l= [] #empty list where values for shared dates will go
    bl=[] #empty list that will have lists added to it
    count= 0 #count which will be useful in indexing later

    for a in stock_dict: #looks for a date in a dictionary
        if a in rain_dict: #looks for a date also in another dictionary
            l.append(stock_dict[a]) #adds value from first dictionary to empty list
            l.append(rain_dict[a]) #adds value from second dictionary to empty list

    number_of_lists= int(len(l)/2) #calculates number of lists that will go into the empty list

    for i in range (0,number_of_lists): #adds number of empty lists to empty list
        bl.append([])
        for x in range(0,2): #adds values from list to nested list
            count = count + 1
            bl[i].append(l[count-1])
    return bl #returns nested list


def scatter_plot(data, format, name, done):
    # TODO:
    #  1. write the complete docstring of this function.
    #  2. implement this function as specified in the handout
    """
    creates a scatter plot with rainfall data as x value and stock data as y values
    param data: (list) a nested list with stock data and rainfall data as entries
    param format: (str) a format for matplotlib
    param name: (str) a name of stock
    param done: (bool) a boolean that is true if the data is the final plot
    """
    count=0 #useful for the indices
    y=[] #empty list for y values
    x=[] #empty list for x values

    for i in data: #adds the y and x values into their respective lists
        count= count +1
        y.append(data[count-1][0])
        x.append(data[count-1][1])

    plt.xlabel("Rainfall")  #labels x axis
    plt.ylabel("price change") #labels y axis
    plt.title("Rainfall vs Price change") #adds title label
    plt.plot(x,y, format, label= name) #plots data

    if done==True: #shows plot when done
        plt.legend()
        plt.show()




def main():
    """
    1. Ask the user for an input of a rainfall data file
    2. Ask the user for an input of a stock data file
    3. Ask the user for two stock symbols
        Note: One of them should be either Microsoft (MSFT) or 
        Amazon (AMZN) headquartered in Seattle, the other should 
        be a company primarily located in elsewhere
    4. Call parse_rainfall and parse_stock for data processing
    5. Call correlated_data and scatter_plot for data analysis and visualizaton
    """
    #ask for needed inputs
    rainfallname= input("Enter the name of a rainfall data file:\n\t")
    stockname= input("Enter the name of a stock data file:\n\t")
    symbol_one= input("Enter a first stock symbol (e.g. MSFT or AMZN):\n\t")
    symbol_two= input("Enter a second stock symbol (not head-quartered in Seattle):\n\t")

    #runs functions on inputs to create data
    rainfalldata= parse_rainfall(rainfallname)
    stockdata_one= parse_stock(stockname,symbol_one)
    stockdata_two= parse_stock(stockname,symbol_two)



    #plots data
    scatter_plot(correlate_data(stockdata_one, rainfalldata),"b.", symbol_one, False)
    scatter_plot(correlate_data(stockdata_two, rainfalldata), "r+", symbol_two, True)

if __name__ == "__main__":
    main()
    import sys
    if len(sys.argv) == 1:
        plt.show()
    else:
        plt.savefig(sys.argv[1])

