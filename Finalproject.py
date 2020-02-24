# Aubrey Jenkins
#CSCI 431
#Finalproject.py
#Thos program uses data that is read from a spreadsheet that comes in as a CSV then goes through the data and finds the best Criteria that i am looking for
#For Auto mode i Give the top Three of each criteria that i am looking at and display those with some flights in each
#For manual I filter based on what the user wants

import Tkinter as tk
import pandas as pan
import ttk
import operator
################################################
#
def getCombo1(Dat):# This Function Takes Month data for each of the top Months and Then finds the best Carrier in each of those months
    using=Dat[["DEPARTURES_SCHEDULED","DEPARTURES_PERFORMED","SEATS","DISTANCE","CARRIER_NAME"]]# Get the Coulmns That I will be Working With# Get the Coulmns That I will be Working With
    usinglist=using.values.tolist()# Turn the Data into A list That i can work with
    CombList=using.CARRIER_NAME.unique()# Gets the Unique names for Carriers That are In that month
    Combo=[]# Makes and Empty list that is used to hold lists of the data i need
    Comb= ""
    i=0
    while i< len(CombList):
        extra=["",0,0,0,0,0]#creates an array that will hold the Name of the criteria i want and all the values that i will manipulate
        extra[0]=CombList[i]#puts the Name of the Criteria in the first index of the list
        Combo.append(extra)#adds it to another list that i will manipute later
        i+=1
    for Sch,Per,Seat,Dist,CN in usinglist:
        for CL in Combo :
            if CN == CL[0]:
                CL[1] = CL[1] + float(Sch)#hold scheduled
                CL[2] = CL[2] + float(Per)#hold Performed
                CL[3] = CL[3] + int(Seat)#Hold Seats

    for C in Combo:
        C[3]=C[3]/C[2]#average number of seats for each month
        C[4]=C[2]/C[1]# Sucess Rate of The Criteria
        C[5]=(C[3]*C[4])*C[2]# Calcualtes the Score That I would Get =


    Combo=sorted(Combo, key=operator.itemgetter(5), reverse=True)#sort by the score
    Comb=Combo[0][0]
    return Comb

def getCombo2(Dat):# This Function Takes Carrier Data and finds the best Origin city fro each of the best Carriers
    using=Dat[["DEPARTURES_SCHEDULED","DEPARTURES_PERFORMED","SEATS","DISTANCE","CARRIER_NAME","ORIGIN_CITY_NAME"]]# Get the Coulmns That I will be Working With
    usinglist=using.values.tolist()# Turn the Data into A list That i can work with
    CombList=using.ORIGIN_CITY_NAME.unique()# Gets the Unique names for Orgin in each of the Carrier
    Combo=[]# Makes and Empty list that is used to hold lists of the data i need
    Comb= ""
    i=0
    while i< len(CombList):
        extra=["",0,0,0,0,0]
        extra[0]=CombList[i]
        Combo.append(extra)
        i+=1
    for Sch,Per,Seat,Dist,CN,OCN in usinglist:
        for CL in Combo :
            if OCN == CL[0]:
                CL[1] = CL[1] + float(Sch)#hold scheduled
                CL[2] = CL[2] + float(Per)#hold Performed
                CL[3] = CL[3] + int(Seat)#Hold Seats

    for C in Combo:
        C[3]=C[3]/C[2]#average number of seats for each month
        C[4]=C[2]/C[1]# Sucess
        C[5]=(C[3]*C[4])*C[2]
    Combo=sorted(Combo, key=operator.itemgetter(5), reverse=True)
    Comb=Combo[0][0]
    return Comb

def getCombo3(Dat):# This Function Takes Destination Sate data for each of the top Destination Sates and Then finds the best Month in each of those Destination States
    using=Dat[["DEPARTURES_SCHEDULED","DEPARTURES_PERFORMED","SEATS","DISTANCE","MONTH",]]# Get the Coulmns That I will be Working With
    usinglist=using.values.tolist()# Turn the Data into A list That i can work with
    CombList=using.MONTH.unique()# Gets the Unique names for Months That are In that Destination Satate
    Combo=[]# Makes and Empty list that is used to hold lists of the data i need
    Comb= ""
    i=0
    while i< len(CombList):
        extra=["",0,0,0,0,0]
        extra[0]=CombList[i]
        Combo.append(extra)
        i+=1
    for Sch,Per,Seat,Dist,Mon in usinglist:
        for CL in Combo :
            if Mon == CL[0]:
                CL[1] = CL[1] + float(Sch)#hold scheduled
                CL[2] = CL[2] + float(Per)#hold Performed
                CL[3] = CL[3] + int(Seat)#Hold Seats

    for C in Combo:
        C[3]=C[3]/C[2]#average number of seats for each month
        C[4]=C[2]/C[1]# Sucess
        C[5]=(C[3]*C[4])*C[2]


    Combo=sorted(Combo, key=operator.itemgetter(5), reverse=True)
    Comb=Combo[0][0]
    return Comb

def get_man():

    mandata=data#sets maunal data to the data in the list

    if manVar1.get() != "NONE":# if the user actually chose something
        data_filt4=(mandata["DISTANCE_RANGE"]==manVar1.get())#Filters out the data based on the users choice for criteria
        mandata=mandata[data_filt4]
    if manVar2.get() != "NONE":
        data_filt4=(mandata["MONTH"]==manVar2.get())
        mandata=mandata[data_filt4]
    if manVar4.get() != "NONE":
        data_filt4=(mandata["DEST_STATE_NM"]==manVar4.get())
        mandata=mandata[data_filt4]


    if mandata.empty:# if the combonation the user chose came bac with no results
        manEmpty = tk.Toplevel(windowman)
        windowman.title('Sorry')
        emptyText = tk.Text(manEmpty,height=10, width=40)
        emptyText.insert(tk.END, 'Sorry there no Flights that meet these \nRequirements')
        emptyText.pack()
        quitButton = tk.Button(manEmpty, text ='Exit', command=root.quit)
        quitButton.pack()
    else:
        mandata=mandata.sort_values(by=['RATING','SEATS'],ascending=False)#sort by Score then by seats
        mandata = mandata[["SEATS","DISTANCE","CARRIER_NAME","ORIGIN_CITY_NAME","DEST_CITY_NAME","MONTH","RATING"]]#data that i want to show to the user
        manResults = tk.Toplevel(windowman)
        manResults.title('The Results')
        # manResults.configure(background='red')
        resultText = tk.Text(manResults,height=20, width=115)
        mandata=mandata.iloc[0:10,:]
        resultText.insert(tk.END,mandata.to_string(index=False))
        resultText.pack()
        resultText.configure(state="disabled")
        quitButton = tk.Button(manResults, text ='Exit', command=root.quit)
        quitButton.pack()
    #root.quit()

####################################################

#Not Fully Commented becasue it is more part of the final project
#
def create_Manual():
    global windowman
    windowman = tk.Toplevel(root)
    windowman.title('Manul Option')

    manVar1.set("NONE") # initial value
    manVar2.set("NONE") # initial value
    manVar3.set("NONE") # initial value
    manVar4.set("NONE") # initial value
    manVar5.set("NONE") # initial value
    manVar6.set("NONE") # initial value
    ##############
    tk.Label(windowman, text='Distance').grid(row=0)
    option = tk.OptionMenu(windowman, manVar1,"0-99","100-199","200-299","300-399","400-499","500-999","1000-1499","1500-1999","2000-2499","2500-2999","3000-3499","3500-3999","4000-4499","4500-4999")
    option.grid(row=0,column=1)
    ############
    tk.Label(windowman, text='Month').grid(row=1)
    option = tk.OptionMenu(windowman, manVar2,"January","February","March","April","May","June","July","August","September","October","November","December")
    option.grid(row=1,column=1)

    tk.Label(windowman, text='Destination State').grid(row=2)
    option= tk.OptionMenu(windowman,manVar4, "Alabama", "Arkansas", "Arizona","California" ,"Colorado", "Connecticut", "Florida", "Georgia", "Iowa" ,"Idaho",
    "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts","Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi",
    "Nebraska", "New Hampshire", "New Jersey", "New Mexico" ,"Nevada", "New York","North Carolina","Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island","South Carolina",
    "South Dakota", "Tennessee", "Texas", "Utah", "Virginia","U.S. Virgin Islands" ,"Vermont", "Washington", "Wisconsin", "West Virginia")
    option.grid(row=2,column=1)


    button = tk.Button(windowman, text="Calculate", command=get_man)
    button.grid(row=3)


##################################################
#The Automatic Option
def create_Auto():
    windowauto = tk.Toplevel(root) # creates the automatci window
    windowauto.title('Automatic Option')#sets the title of the window

    nb = ttk.Notebook(windowauto)#creates a notebooks that can be used for Tabs

    nb.grid(row=0,column=0, columnspan=30,rowspan=30, sticky='NESW')
    page1 = ttk.Frame(nb)
    nb.add(page1, text= 'Month')

    page2 = ttk.Frame(nb)
    page2.grid(row=0,column=1)
    nb.add(page2, text= 'Destination State')

    page3 = ttk.Frame(nb)
    page3.grid(row=0,column=2)
    nb.add(page3, text= 'Destination City')

    page4 = ttk.Frame(nb)
    page4.grid(row=0,column=3)
    nb.add(page4, text= 'Origin State')

    page5 = ttk.Frame(nb)
    page5.grid(row=0,column=4)
    nb.add(page5, text= 'Origin City')

    page6 = ttk.Frame(nb)
    page6.grid(row=0,column=5)
    nb.add(page6, text= 'AirCraft')

    page7 = ttk.Frame(nb)
    page7.grid(row=0,column=6)
    nb.add(page7, text= 'Distance Range')

    page8 = ttk.Frame(nb)
    page8.grid(row=0,column=7)
    nb.add(page8, text= 'Carrier')

    CombMVar="" # create empty strings to use to hold the name of the best for the combnation
    CombMVar2=""
    CombMVar3=""
    CombCVar=""
    CombCVar2=""
    CombCVar3=""
    CombDVar=""
    CombDVar2=""
    CombDVar3=""
    data["SEATS"]=data["SEATS"]/data["DEPARTURES_PERFORMED"]#makes seats into the actually number of seats by taking Seats/Departures Perfromed

    Monthdata = data# used to hold the data to edit it
    Monthdata2 = data
    Monthdata3 = data

    Cardata = data# used to hold the data to edit it
    Cardata2 = data
    Cardata3 = data

    DRdata = data
    DRdata2 = data
    DRdata3 = data

    DSdata = data
    DSdata2 = data
    DSdata3 = data

    DCdata = data
    DCdata2 = data
    DCdata3 = data

    OSdata = data
    OSdata2 = data
    OSdata3 = data

    OCdata = data
    OCdata2 = data
    OCdata3 = data

    ATdata = data
    ATdata2 = data
    ATdata3 = data

    Monthfilt=(Monthdata["MONTH"]==Month)# creates a filter for the best month
    Monthfilt2=(Monthdata["MONTH"]==Month2)
    Monthfilt3=(Monthdata["MONTH"]==Month3)

    Carfilt=(Cardata["CARRIER_NAME"]==Car)# creates a filter for the best carrier
    Carfilt2=(Cardata["CARRIER_NAME"]==Car2)
    Carfilt3=(Cardata["CARRIER_NAME"]==Car3)

    Monthdata= Monthdata[Monthfilt]# filters out all other months
    Monthdata2= Monthdata2[Monthfilt2]
    Monthdata3= Monthdata3[Monthfilt3]

    CombMVar=getCombo1(Monthdata)#gets the combination that i am going to use and stores it to a variable
    CombMVar2=getCombo1(Monthdata2)
    CombMVar3=getCombo1(Monthdata3)

    Monthdata= Monthdata[Monthdata["CARRIER_NAME"]==CombMVar]#get the combination data
    Monthdata2= Monthdata2[Monthdata2["CARRIER_NAME"]==CombMVar2]
    Monthdata3= Monthdata3[Monthdata3["CARRIER_NAME"]==CombMVar3]

    Cardata= Cardata[Carfilt]
    Cardata2= Cardata2[Carfilt2]
    Cardata3= Cardata3[Carfilt3]

    CombCVar=getCombo2(Cardata)
    CombCVar2=getCombo2(Cardata2)
    CombCVar3=getCombo2(Cardata3)


    Cardata= Cardata[Cardata["ORIGIN_CITY_NAME"]==CombCVar]
    Cardata2= Cardata2[Cardata2["ORIGIN_CITY_NAME"]==CombCVar2]
    Cardata3= Cardata3[Cardata3["ORIGIN_CITY_NAME"]==CombCVar3]



    DRdata= DRdata[DRdata["DISTANCE_RANGE"]==DRange]#gets the flights that meet this criteria that is one of the best
    DRdata2= DRdata2[DRdata2["DISTANCE_RANGE"]==DRange2]
    DRdata3= DRdata3[DRdata3["DISTANCE_RANGE"]==DRange3]


    DSdata= DSdata[DSdata["DEST_STATE_NM"]==DState]
    DSdata2= DSdata2[DSdata2["DEST_STATE_NM"]==DState2]
    DSdata3= DSdata3[DSdata3["DEST_STATE_NM"]==DState3]

    CombDVar=getCombo3(DSdata)
    CombDVar2=getCombo3(DSdata2)
    CombDVar3=getCombo3(DSdata3)


    DSdata= DSdata[DSdata["MONTH"]==CombDVar]
    DSdata2= DSdata2[DSdata2["MONTH"]==CombDVar2]
    DSdata3= DSdata3[DSdata3["MONTH"]==CombDVar3]

    DCdata= DCdata[DCdata["DEST_CITY_NAME"]==DCity]
    DCdata2= DCdata2[DCdata2["DEST_CITY_NAME"]==DCity2]
    DCdata3= DCdata3[DCdata3["DEST_CITY_NAME"]==DCity3]

    OSdata= OSdata[OSdata["ORIGIN_STATE_NM"]==OState]
    OSdata2= OSdata2[OSdata2["ORIGIN_STATE_NM"]==OState2]
    OSdata3= OSdata3[OSdata3["ORIGIN_STATE_NM"]==OState3]

    OCdata= OCdata[OCdata["ORIGIN_CITY_NAME"]==OCity]
    OCdata2= OCdata2[OCdata2["ORIGIN_CITY_NAME"]==OCity2]
    OCdata3= OCdata3[OCdata3["ORIGIN_CITY_NAME"]==OCity3]

    ATdata= ATdata[ATdata["AIRCRAFT_TYPE"]==ACraft]
    ATdata2= ATdata2[ATdata2["AIRCRAFT_TYPE"]==ACraft2]
    ATdata3= ATdata3[ATdata3["AIRCRAFT_TYPE"]==ACraft3]



    Monthdata=Monthdata.sort_values(by=['RATING','SEATS'],ascending=False) # sorts the flights by there rating then by seats
    Monthdata2=Monthdata2.sort_values(by=['RATING','SEATS'],ascending=False) # sorts the flights by there rating then by seats
    Monthdata3=Monthdata3.sort_values(by=['RATING','SEATS'],ascending=False) # sorts the flights by there rating then by seats

    Cardata=Cardata.sort_values(by=['RATING','SEATS'],ascending=False) # sorts the flights by there rating then by seats
    Cardata2=Cardata2.sort_values(by=['RATING','SEATS'],ascending=False) # sorts the flights by there rating then by seats
    Cardata3=Cardata3.sort_values(by=['RATING','SEATS'],ascending=False) # sorts the flights by there rating then by seats

    DRdata=DRdata.sort_values(by=['RATING','SEATS'],ascending=False) # sorts the flights by there rating then by seats
    DRdata2=DRdata2.sort_values(by=['RATING','SEATS'],ascending=False) # sorts the flights by there rating then by seats
    DRdata3=DRdata3.sort_values(by=['RATING','SEATS'],ascending=False) # sorts the flights by there rating then by seats

    DSdata=DSdata.sort_values(by=['RATING','SEATS'],ascending=False) # sorts the flights by there rating then by seats
    DSdata2=DSdata2.sort_values(by=['RATING','SEATS'],ascending=False) # sorts the flights by there rating then by seats
    DSdata3=DSdata3.sort_values(by=['RATING','SEATS'],ascending=False) # sorts the flights by there rating then by seats

    DCdata=DCdata.sort_values(by=['RATING','SEATS'],ascending=False) # sorts the flights by there rating then by seats
    DCdata2=DCdata2.sort_values(by=['RATING','SEATS'],ascending=False) # sorts the flights by there rating then by seats
    DCdata3=DCdata3.sort_values(by=['RATING','SEATS'],ascending=False) # sorts the flights by there rating then by seats

    OSdata=OSdata.sort_values(by=['RATING','SEATS'],ascending=False) # sorts the flights by there rating then by seats
    OSdata2=OSdata2.sort_values(by=['RATING','SEATS'],ascending=False) # sorts the flights by there rating then by seats
    OSdata3=OSdata3.sort_values(by=['RATING','SEATS'],ascending=False) # sorts the flights by there rating then by seats

    OCdata=OCdata.sort_values(by=['RATING','SEATS'],ascending=False) # sorts the flights by there rating then by seats
    OCdata2=OCdata2.sort_values(by=['RATING','SEATS'],ascending=False) # sorts the flights by there rating then by seats
    OCdata3=OCdata3.sort_values(by=['RATING','SEATS'],ascending=False) # sorts the flights by there rating then by seats

    ATdata=ATdata.sort_values(by=['RATING','SEATS'],ascending=False) # sorts the flights by there rating then by seats
    ATdata2=ATdata2.sort_values(by=['RATING','SEATS'],ascending=False) # sorts the flights by there rating then by seats
    ATdata3=ATdata3.sort_values(by=['RATING','SEATS'],ascending=False) # sorts the flights by there rating then by seats



    MonthVar="The Best Month is: " + Month + " \nThe Best Carrier For the Month is: " + CombMVar + "\n\n"
    MonthVar2="\n\nThe Second Best Month is  : " + Month2 + " \nThe Best Carrier For the Month is: " + CombMVar2 + "\n\n"
    MonthVar3="\n\nThe Third Best Month is: " + Month3 + " \nThe Best Carrier For the Month is: " + CombMVar3 + "\n\n"

    CarVar="The Best Carrier is: " + Car + "\nThe Best Origin City for This Carrier is:" + CombCVar +"\n\n"
    CarVar2="\n\nThe Second Best Carrier is  : " + Car2 + "\nThe Best Origin City for This Carrier is:" + CombCVar2 +"\n\n"
    CarVar3="\n\nThe Third Best Carrier is: " + Car3 + "\nThe Best Origin City for This Carrier is:" + CombCVar3 +"\n\n"

    DRVar="The Best Distance Range is: " + DRange + "\n\n"
    DRVar2="\n\nThe Second Best Distance Range is  : " + DRange2 + "\n\n"
    DRVar3="\n\nThe Third Best Distance Range is: " + DRange3 + "\n\n"

    DSVar="The Best Destination State is: " + DState + "\n The Best Month To fly to this State is: " + CombDVar +"\n\n"
    DSVar2="\n\nThe Second Best Destination State is  : " + DState2 + "\n The Best Month To fly to this State is: " + CombDVar +"\n\n"
    DSVar3="\n\nThe Third Best Destination State is: " + DState3 + "\n The Best Month To fly to this State is: " + CombDVar +"\n\n"

    DCVar="The Best Destination City is: " + DCity + "\n\n"
    DCVar2="\n\nThe Second Best Destination City is  : " + DCity2 + "\n\n"
    DCVar3="\n\nThe Third Best Destination City is: " + DCity3 + "\n\n"

    OSVar="The Best Origin State is: " + OState + "\n\n"
    OSVar2="\n\nThe Second Best Origin State is  : " + OState2 + "\n\n"
    OSVar3="\n\nThe Third Best Origin State is: " + OState3 + "\n\n"

    OCVar="The Best Origin City is: " + OCity + "\n\n"
    OCVar2="\n\nThe Second Best Origin City is  : " + OCity2 + "\n\n"
    OCVar3="\n\nThe Third Best Origin City is: " + OCity3 + "\n\n"

    ATVar="The Best Air Craft is: " + str(ACraft) + "\n\n"
    ATVar2="\n\nThe Second Best Air Craft is  : " + str(ACraft2) + "\n\n"
    ATVar3="\n\nThe Third Best Air Craft is: " + str(ACraft3) + "\n\n"




    Monthdata = Monthdata[["SEATS","DISTANCE","CARRIER_NAME","ORIGIN_CITY_NAME","DEST_CITY_NAME","MONTH","RATING","AVERAGE_SUCCESS_FOR_MONTH","OVERALL_RATING_FOR_MONTH"]]# gets only the colums that i want
    Monthdata2 = Monthdata2[["SEATS","DISTANCE","CARRIER_NAME","ORIGIN_CITY_NAME","DEST_CITY_NAME","MONTH","RATING","AVERAGE_SUCCESS_FOR_MONTH","OVERALL_RATING_FOR_MONTH"]]# gets only the colums that i want
    Monthdata3 = Monthdata3[["SEATS","DISTANCE","CARRIER_NAME","ORIGIN_CITY_NAME","DEST_CITY_NAME","MONTH","RATING","AVERAGE_SUCCESS_FOR_MONTH","OVERALL_RATING_FOR_MONTH"]]# gets only the colums that i want

    Cardata = Cardata[["SEATS","DISTANCE","CARRIER_NAME","ORIGIN_CITY_NAME","DEST_CITY_NAME","MONTH","RATING","AVERAGE_SUCCESS_FOR_CARRIER","OVERALL_RATING_FOR_CARRIER"]]# gets only the colums that i want
    Cardata2 = Cardata2[["SEATS","DISTANCE","CARRIER_NAME","ORIGIN_CITY_NAME","DEST_CITY_NAME","MONTH","RATING","AVERAGE_SUCCESS_FOR_CARRIER","OVERALL_RATING_FOR_CARRIER"]]# gets only the colums that i want
    Cardata3 = Cardata3[["SEATS","DISTANCE","CARRIER_NAME","ORIGIN_CITY_NAME","DEST_CITY_NAME","MONTH","RATING","AVERAGE_SUCCESS_FOR_CARRIER","OVERALL_RATING_FOR_CARRIER"]]# gets only the colums that i want

    DRdata = DRdata[["SEATS","DISTANCE","CARRIER_NAME","ORIGIN_CITY_NAME","DEST_CITY_NAME","MONTH","RATING","DISTANCE_RANGE","AVERAGE_SUCCESS_FOR_DISTANCE","OVERALL_RATING_FOR_DISTANCE"]]# gets only the colums that i want
    DRdata2 = DRdata2[["SEATS","DISTANCE","CARRIER_NAME","ORIGIN_CITY_NAME","DEST_CITY_NAME","MONTH","RATING","DISTANCE_RANGE","AVERAGE_SUCCESS_FOR_DISTANCE","OVERALL_RATING_FOR_DISTANCE"]]# gets only the colums that i want
    DRdata3 = DRdata3[["SEATS","DISTANCE","CARRIER_NAME","ORIGIN_CITY_NAME","DEST_CITY_NAME","MONTH","RATING","DISTANCE_RANGE","AVERAGE_SUCCESS_FOR_DISTANCE","OVERALL_RATING_FOR_DISTANCE"]]# gets only the colums that i want

    DSdata = DSdata[["SEATS","DISTANCE","CARRIER_NAME","ORIGIN_CITY_NAME","DEST_CITY_NAME","MONTH","RATING","AVERAGE_SUCCESS_FOR_DEST_STATE","OVERALL_RATING_FOR_DEST_STATE"]]# gets only the colums that i want
    DSdata2 = DSdata2[["SEATS","DISTANCE","CARRIER_NAME","ORIGIN_CITY_NAME","DEST_CITY_NAME","MONTH","RATING","AVERAGE_SUCCESS_FOR_DEST_STATE","OVERALL_RATING_FOR_DEST_STATE"]]# gets only the colums that i want
    DSdata3 = DSdata3[["SEATS","DISTANCE","CARRIER_NAME","ORIGIN_CITY_NAME","DEST_CITY_NAME","MONTH","RATING","AVERAGE_SUCCESS_FOR_DEST_STATE","OVERALL_RATING_FOR_DEST_STATE"]]# gets only the colums that i want

    DCdata = DCdata[["SEATS","DISTANCE","CARRIER_NAME","ORIGIN_CITY_NAME","DEST_CITY_NAME","MONTH","RATING","AVERAGE_SUCCESS_FOR_DEST_CITY","OVERALL_RATING_FOR_DEST_CITY"]]# gets only the colums that i want
    DCdata2 = DCdata2[["SEATS","DISTANCE","CARRIER_NAME","ORIGIN_CITY_NAME","DEST_CITY_NAME","MONTH","RATING","AVERAGE_SUCCESS_FOR_DEST_CITY","OVERALL_RATING_FOR_DEST_CITY"]]# gets only the colums that i want
    DCdata3 = DCdata3[["SEATS","DISTANCE","CARRIER_NAME","ORIGIN_CITY_NAME","DEST_CITY_NAME","MONTH","RATING","AVERAGE_SUCCESS_FOR_DEST_CITY","OVERALL_RATING_FOR_DEST_CITY"]]# gets only the colums that i want

    OSdata = OSdata[["SEATS","DISTANCE","CARRIER_NAME","ORIGIN_CITY_NAME","DEST_CITY_NAME","MONTH","RATING","DISTANCE_RANGE","AVERAGE_SUCCESS_FOR_ORIGIN_STATE","OVERALL_RATING_FOR_ORIGIN_STATE"]]# gets only the colums that i want
    OSdata2 = OSdata2[["SEATS","DISTANCE","CARRIER_NAME","ORIGIN_CITY_NAME","DEST_CITY_NAME","MONTH","RATING","DISTANCE_RANGE","AVERAGE_SUCCESS_FOR_ORIGIN_STATE","OVERALL_RATING_FOR_ORIGIN_STATE"]]# gets only the colums that i want
    OSdata3 = OSdata3[["SEATS","DISTANCE","CARRIER_NAME","ORIGIN_CITY_NAME","DEST_CITY_NAME","MONTH","RATING","DISTANCE_RANGE","AVERAGE_SUCCESS_FOR_ORIGIN_STATE","OVERALL_RATING_FOR_ORIGIN_STATE"]]# gets only the colums that i want

    OCdata = OCdata[["SEATS","DISTANCE","CARRIER_NAME","ORIGIN_CITY_NAME","DEST_CITY_NAME","MONTH","RATING","AVERAGE_SUCCESS_FOR_ORIGIN_CITY","OVERALL_RATING_FOR_ORIGIN_CITY"]]# gets only the colums that i want
    OCdata2 = OCdata2[["SEATS","DISTANCE","CARRIER_NAME","ORIGIN_CITY_NAME","DEST_CITY_NAME","MONTH","RATING","AVERAGE_SUCCESS_FOR_ORIGIN_CITY","OVERALL_RATING_FOR_ORIGIN_CITY"]]# gets only the colums that i want
    OCdata3 = OCdata3[["SEATS","DISTANCE","CARRIER_NAME","ORIGIN_CITY_NAME","DEST_CITY_NAME","MONTH","RATING","AVERAGE_SUCCESS_FOR_ORIGIN_CITY","OVERALL_RATING_FOR_ORIGIN_CITY"]]# gets only the colums that i want

    ATdata = ATdata[["SEATS","DISTANCE","CARRIER_NAME","ORIGIN_CITY_NAME","DEST_CITY_NAME","MONTH","AIRCRAFT_TYPE","RATING","AVERAGE_SUCCESS_FOR_AIR_CRAFT","OVERALL_RATING_FOR_AIR_CRAFT"]]# gets only the colums that i want
    ATdata2 = ATdata2[["SEATS","DISTANCE","CARRIER_NAME","ORIGIN_CITY_NAME","DEST_CITY_NAME","MONTH","AIRCRAFT_TYPE","RATING","AVERAGE_SUCCESS_FOR_AIR_CRAFT","OVERALL_RATING_FOR_AIR_CRAFT"]]# gets only the colums that i want
    ATdata3 = ATdata3[["SEATS","DISTANCE","CARRIER_NAME","ORIGIN_CITY_NAME","DEST_CITY_NAME","MONTH","AIRCRAFT_TYPE","RATING","AVERAGE_SUCCESS_FOR_AIR_CRAFT","OVERALL_RATING_FOR_AIR_CRAFT"]]# gets only the colums that i want

    MonthresultText = tk.Text(page1,height=30, width=170)
    MonthresultText.insert(tk.END,MonthVar)# inserts the text into the window
    Monthdata=Monthdata.iloc[0:5,:]# extracts only the first flight
    MonthresultText.insert(tk.END,Monthdata.to_string(index=False)) # Puts the data into the gui

    MonthresultText.insert(tk.END,MonthVar2)# inserts the text into the window
    Monthdata2=Monthdata2.iloc[0:5,:]# extracts only the first flight
    MonthresultText.insert(tk.END,Monthdata2.to_string(index=False)) # Puts the data into the gui

    MonthresultText.insert(tk.END,MonthVar3)# inserts the text into the window
    Monthdata3=Monthdata3.iloc[0:5,:]# extracts only the first flight
    MonthresultText.insert(tk.END,Monthdata3.to_string(index=False)) # Puts the data into the gui

    MonthresultText.grid(row=3,column=1)
    MonthresultText.configure(state='disabled')


    CarresultText = tk.Text(page8,height=30, width=170)
    CarresultText.insert(tk.END,CarVar)# inserts the text into the window
    Cardata=Cardata.iloc[0:5,:]# extracts only the first flight
    CarresultText.insert(tk.END,Cardata.to_string(index=False)) # Puts the data into the gui

    CarresultText.insert(tk.END,CarVar2)# inserts the text into the window
    Cardata2=Cardata2.iloc[0:5,:]# extracts only the first flight
    CarresultText.insert(tk.END,Cardata2.to_string(index=False)) # Puts the data into the gui

    CarresultText.insert(tk.END,CarVar3)# inserts the text into the window
    Cardata3=Cardata3.iloc[0:5,:]# extracts only the first flight
    CarresultText.insert(tk.END,Cardata3.to_string(index=False)) # Puts the data into the gui

    CarresultText.grid(row=3,column=1)
    CarresultText.configure(state='disabled')

    DRresultText = tk.Text(page7,height=30, width=200)
    DRresultText.insert(tk.END,DRVar)# inserts the text into the window
    DRdata=DRdata.iloc[0:5,:]# extracts only the first flight
    DRresultText.insert(tk.END,DRdata.to_string(index=False)) # Puts the data into the gui

    DRresultText.insert(tk.END,DRVar2)# inserts the text into the window
    DRdata2=DRdata2.iloc[0:5,:]# extracts only the first flight
    DRresultText.insert(tk.END,DRdata2.to_string(index=False)) # Puts the data into the gui

    DRresultText.insert(tk.END,DRVar3)# inserts the text into the window
    DRdata3=DRdata3.iloc[0:5,:]# extracts only the first flight
    DRresultText.insert(tk.END,DRdata3.to_string(index=False)) # Puts the data into the gui

    DRresultText.grid(row=3,column=1)
    DRresultText.configure(state='disabled')

    DSresultText = tk.Text(page2,height=30, width=180)
    DSresultText.insert(tk.END,DSVar)# inserts the text into the window
    DSdata=DSdata.iloc[0:5,:]# extracts only the first flight
    DSresultText.insert(tk.END,DSdata.to_string(index=False)) # Puts the data into the gui

    DSresultText.insert(tk.END,DSVar2)# inserts the text into the window
    DSdata2=DSdata2.iloc[0:5,:]# extracts only the first flight
    DSresultText.insert(tk.END,DSdata2.to_string(index=False)) # Puts the data into the gui

    DSresultText.insert(tk.END,DSVar3)# inserts the text into the window
    DSdata3=DSdata3.iloc[0:5,:]# extracts only the first flight
    DSresultText.insert(tk.END,DSdata3.to_string(index=False)) # Puts the data into the gui

    DSresultText.grid(row=3,column=1)
    DSresultText.configure(state='disabled')

    DCresultText = tk.Text(page3,height=30, width=170)
    DCresultText.insert(tk.END,DCVar)# inserts the text into the window
    DCdata=DCdata.iloc[0:5,:]# extracts only the first flight
    DCresultText.insert(tk.END,DCdata.to_string(index=False)) # Puts the data into the gui

    DCresultText.insert(tk.END,DCVar2)# inserts the text into the window
    DCdata2=DCdata2.iloc[0:5,:]# extracts only the first flight
    DCresultText.insert(tk.END,DCdata2.to_string(index=False)) # Puts the data into the gui

    DCresultText.insert(tk.END,DCVar3)# inserts the text into the window
    DCdata3=DCdata3.iloc[0:5,:]# extracts only the first flight
    DCresultText.insert(tk.END,DCdata3.to_string(index=False)) # Puts the data into the gui

    DCresultText.grid(row=3,column=1)
    DCresultText.configure(state='disabled')

    OSresultText = tk.Text(page4,height=30, width=200)
    OSresultText.insert(tk.END,OSVar)# inserts the text into the window
    OSdata=OSdata.iloc[0:5,:]# extracts only the first flight
    OSresultText.insert(tk.END,OSdata.to_string(index=False)) # Puts the data into the gui

    OSresultText.insert(tk.END,OSVar2)# inserts the text into the window
    OSdata2=OSdata2.iloc[0:5,:]# extracts only the first flight
    OSresultText.insert(tk.END,OSdata2.to_string(index=False)) # Puts the data into the gui

    OSresultText.insert(tk.END,OSVar3)# inserts the text into the window
    OSdata3=OSdata3.iloc[0:5,:]# extracts only the first flight
    OSresultText.insert(tk.END,OSdata3.to_string(index=False)) # Puts the data into the gui

    OSresultText.grid(row=3,column=1)
    OSresultText.configure(state='disabled')

    OCresultText = tk.Text(page5,height=30, width=180)
    OCresultText.insert(tk.END,OCVar)# inserts the text into the window
    OCdata=OCdata.iloc[0:5,:]# extracts only the first flight
    OCresultText.insert(tk.END,OCdata.to_string(index=False)) # Puts the data into the gui

    OCresultText.insert(tk.END,OCVar2)# inserts the text into the window
    OCdata2=OCdata2.iloc[0:5,:]# extracts only the first flight
    OCresultText.insert(tk.END,OCdata2.to_string(index=False)) # Puts the data into the gui

    OCresultText.insert(tk.END,OCVar3)# inserts the text into the window
    OCdata3=OCdata3.iloc[0:5,:]# extracts only the first flight
    OCresultText.insert(tk.END,OCdata3.to_string(index=False)) # Puts the data into the gui

    OCresultText.grid(row=3,column=1)
    OCresultText.configure(state='disabled')

    ATresultText = tk.Text(page6,height=30, width=190)
    ATresultText.insert(tk.END,ATVar)# inserts the text into the window
    ATdata=ATdata.iloc[0:5,:]# extracts only the first flight
    ATresultText.insert(tk.END,ATdata.to_string(index=False)) # Puts the data into the gui

    ATresultText.insert(tk.END,ATVar2)# inserts the text into the window
    ATdata2=ATdata2.iloc[0:5,:]# extracts only the first flight
    ATresultText.insert(tk.END,ATdata2.to_string(index=False)) # Puts the data into the gui

    ATresultText.insert(tk.END,ATVar3)# inserts the text into the window
    ATdata3=ATdata3.iloc[0:5,:]# extracts only the first flight
    ATresultText.insert(tk.END,ATdata3.to_string(index=False)) # Puts the data into the gui

    ATresultText.grid(row=3,column=1)
    ATresultText.configure(state='disabled')

    quitButton = tk.Button(windowauto, text ='Exit', command=root.quit)
    quitButton.grid(row=40,column=20)

###########################################################

# The main Program
global data # I set it as a global variable so that the functions can see it used for the data that is being read in
global Month,Month2,Month3 # Variable that is used to hold the results of the best month
global Car,Car2,Car3
global DState,DState2,DState3
global DCity,DCity2,DCity3
global OCity,OCity2,OCity3
global OState,OState2,OState3
global DRange,DRange2,DRange3
global ACraft,ACraft2,ACraft3

data = pan.read_csv("projdata.csv")# read in the data so that it can be used

data=data[["DEPARTURES_SCHEDULED","DEPARTURES_PERFORMED","SEATS","DISTANCE","CARRIER_NAME","ORIGIN_STATE_NM","ORIGIN_CITY_NAME","DEST_CITY_NAME","DEST_STATE_NM","AIRCRAFT_TYPE","MONTH"]] #get only the row that i want from the spreadsheet and put it into the data
data_filt=(data["DEPARTURES_SCHEDULED"]>0) #get a filter that is only true when departures scheduled is greater than 0
filtered_data=data[data_filt] #apllies the filter
ratio=filtered_data["DEPARTURES_PERFORMED"]/filtered_data["DEPARTURES_SCHEDULED"] #makes data that has the condition of performed/scheduled
data["My_Ratio"]= ratio# adds a new coulmn to the data that stores the ratio of each row
data_filt2=((data["My_Ratio"]>0)  & (data["My_Ratio"]<=1)) #filters out rations that are zero or greater than 100%
data=data[data_filt2]# applies the filter to the data and sets the data to the new data
data_filt3=(data["SEATS"]>0)# filter out filghts with 0 seats
data=data[data_filt3] #applies filters to data and sets the data to it
stars= (data["SEATS"]/data["DEPARTURES_PERFORMED"])*data["My_Ratio"]*data["DEPARTURES_PERFORMED"] # my formula to calculate a score for the flights that I will use to sort by
data["RATING"]=stars # adds a new coulmn to the data

#Sets the Distance Ranges and makes a new coulmn for it
data.loc[(data.DISTANCE >=0) & (data.DISTANCE < 100)  , 'DISTANCE_RANGE'] = '0-99'
data.loc[(data.DISTANCE >= 100) & (data.DISTANCE < 200)  , 'DISTANCE_RANGE'] = '100-199'
data.loc[(data.DISTANCE >= 200) & (data.DISTANCE < 300)  , 'DISTANCE_RANGE'] = '200-299'
data.loc[(data.DISTANCE >= 300) & (data.DISTANCE < 400)  , 'DISTANCE_RANGE'] = '300-399'
data.loc[(data.DISTANCE >= 400) & (data.DISTANCE < 500)  , 'DISTANCE_RANGE'] = '400-499'
data.loc[(data.DISTANCE >= 500) & (data.DISTANCE < 1000)  , 'DISTANCE_RANGE'] = '500-999'
data.loc[(data.DISTANCE >= 1000) & (data.DISTANCE < 1500)  , 'DISTANCE_RANGE'] = '1000-1499'
data.loc[(data.DISTANCE >= 1500) & (data.DISTANCE < 2000)  , 'DISTANCE_RANGE'] = '1500-1999'
data.loc[(data.DISTANCE >= 2000) & (data.DISTANCE < 2500)  , 'DISTANCE_RANGE'] = '2000-2499'
data.loc[(data.DISTANCE >= 2500) & (data.DISTANCE < 3000)  , 'DISTANCE_RANGE'] = '2500-2999'
data.loc[(data.DISTANCE >= 3000) & (data.DISTANCE < 3500)  , 'DISTANCE_RANGE'] = '3000-3499'
data.loc[(data.DISTANCE >= 3500) & (data.DISTANCE < 4000)  , 'DISTANCE_RANGE'] = '3500-3999'
data.loc[(data.DISTANCE >= 4000) & (data.DISTANCE < 4500)  , 'DISTANCE_RANGE'] = '4000-4499'
data.loc[(data.DISTANCE >= 4500) & (data.DISTANCE < 5000)  , 'DISTANCE_RANGE'] = '4500-4999'

#Changes the months from numbers to their name counterpart and replaces it in the data
data.loc[data.MONTH == 1 , 'MONTH'] = 'January'
data.loc[data.MONTH == 2 , 'MONTH'] = 'February'
data.loc[data.MONTH == 3 , 'MONTH'] = 'March'
data.loc[data.MONTH == 4 , 'MONTH'] = 'April'
data.loc[data.MONTH == 5 , 'MONTH'] = 'May'
data.loc[data.MONTH == 6 , 'MONTH'] = 'June'
data.loc[data.MONTH == 7 , 'MONTH'] = 'July'
data.loc[data.MONTH == 8 , 'MONTH'] = 'August'
data.loc[data.MONTH == 9 , 'MONTH'] = 'September'
data.loc[data.MONTH == 10 , 'MONTH'] = 'October'
data.loc[data.MONTH == 11 , 'MONTH'] = 'November'
data.loc[data.MONTH == 12 , 'MONTH'] = 'December'


flightlist= data.values.tolist()
CarrierList=data.CARRIER_NAME.unique()# Gets the unique names fro each of the following criteria
MonthList= data.MONTH.unique()# Gets the unique names fro each of the following criteria
DestSList= data.DEST_STATE_NM.unique()# Gets the unique names fro each of the following criteria
DestCList= data.DEST_CITY_NAME.unique()# Gets the unique names fro each of the following criteria
OCList= data.ORIGIN_CITY_NAME.unique()# Gets the unique names fro each of the following criteria
AirList= data.AIRCRAFT_TYPE.unique()# Gets the unique names fro each of the following criteria
OSList= data.ORIGIN_STATE_NM.unique()# Gets the unique names fro each of the following criteria
DRList= data.DISTANCE_RANGE.unique()# Gets the unique names fro each of the following criteria


Carriers=[]# Makes an empty list to hold the criteria and data that will go with it
Months=[]# Makes an empty list to hold the criteria and data that will go with it
DestS=[]# Makes an empty list to hold the criteria and data that will go with it
DestC=[]# Makes an empty list to hold the criteria and data that will go with it
OriginC=[]# Makes an empty list to hold the criteria and data that will go with it
OriginS=[]# Makes an empty list to hold the criteria and data that will go with it
DistanceR=[]# Makes an empty list to hold the criteria and data that will go with it
AirCraft=[]# Makes an empty list to hold the criteria and data that will go with it
i=0
while i< len(CarrierList):
    extra=["",0,0,0,0,0]#used to hold the name of the criteria and supporting stats
    extra[0]=CarrierList[i]#gets the name of the criteria
    Carriers.append(extra)#adds it to the bigger list so that i can manipuulate it later
    i+=1
i=0
while i< len(MonthList):
    extra=["",0,0,0,0,0]
    extra[0]=MonthList[i]
    Months.append(extra)
    i+=1
i=0
while i< len(DestSList):
    extra=["",0,0,0,0,0]
    extra[0]=DestSList[i]
    DestS.append(extra)
    i+=1
i=0
while i< len(DestCList):
    extra=["",0,0,0,0,0]
    extra[0]=DestCList[i]
    DestC.append(extra)
    i+=1
i=0
while i< len(OCList):
    extra=["",0,0,0,0,0]
    extra[0]=OCList[i]
    OriginC.append(extra)
    i+=1
i=0
while i< len(OSList):
    extra=["",0,0,0,0,0]
    extra[0]=OSList[i]
    OriginS.append(extra)
    i+=1
i=0
while i< len(DRList):
    extra=["",0,0,0,0,0]
    extra[0]=DRList[i]
    DistanceR.append(extra)
    i+=1
i=0
while i< len(AirList):
    extra=["",0,0,0,0,0]
    extra[0]=AirList[i]
    AirCraft.append(extra)
    i+=1
#going through all of the rows inside of the data list that has been created
#find where values in the data match the criteria that is being looked at and add those stats to that list
for Sch,Per,Seat,Dist,CN,OSN,OCN,DCN,DSN,AT,Mon,Rat,Score,DR in flightlist:
    for CL in Carriers :
        if CN == CL[0]:
            CL[1] = CL[1] + float(Sch)#hold scheduled
            CL[2] = CL[2] + float(Per)#hold Performed
            CL[3] = CL[3] + int(Seat)#Hold Seats

    for Month in Months :
        if Mon == Month[0]:
            Month[1] = Month[1] + float(Sch)#hold scheduled
            Month[2] = Month[2] + float(Per)#hold Performed
            Month[3] = Month[3] + int(Seat)#Hold Seats

    for DistRange in DistanceR :
        if DR == DistRange[0]:
            DistRange[1] = DistRange[1] + float(Sch)#hold scheduled
            DistRange[2] = DistRange[2] + float(Per)#hold Performed
            DistRange[3] = DistRange[3] + int(Seat)#Hold Seats

    for OrSt in OriginS :
        if OSN == OrSt[0]:
            OrSt[1] = OrSt[1] + float(Sch)#hold scheduled
            OrSt[2] = OrSt[2] + float(Per)#hold Performed
            OrSt[3] = OrSt[3] + int(Seat)#Hold Seats

    for OrCn in OriginC :
        if OCN == OrCn[0]:
            OrCn[1] = OrCn[1] + float(Sch)#hold scheduled
            OrCn[2] = OrCn[2] + float(Per)#hold Performed
            OrCn[3] = OrCn[3] + int(Seat)#Hold Seats

    for DesS in DestS :
        if DSN == DesS[0]:
            DesS[1] = DesS[1] + float(Sch)#hold scheduled
            DesS[2] = DesS[2] + float(Per)#hold Performed
            DesS[3] = DesS[3] + int(Seat)#Hold Seats

    for DesC in DestC :
        if DCN == DesC[0]:
            DesC[1] = DesC[1] + float(Sch)#hold scheduled
            DesC[2] = DesC[2] + float(Per)#hold Performed
            DesC[3] = DesC[3] + int(Seat)#Hold Seats

    for AirT in AirCraft :
        if AT == AirT[0]:
            AirT[1] = AirT[1] + float(Sch)#hold scheduled
            AirT[2] = AirT[2] + float(Per)#hold Performed
            AirT[3] = AirT[3] + int(Seat)#Hold Seats

for M in Months:
    M[3]=M[3]/M[2]#average number of seats for each month
    M[4]=M[2]/M[1]#ratio of how likely flights will succed in
    M[5]=(M[3]*M[4])*M[2]#Average Score for the month
for C in Carriers:
    C[3]=C[3]/C[2]#average number of seats for each month
    C[4]=C[2]/C[1]# Sucess
    C[5]=(C[3]*C[4])*C[2]

for OS in OriginS:
    OS[3]=OS[3]/OS[2]#average number of seats for each month
    OS[4]=OS[2]/OS[1]
    OS[5]=(OS[3]*OS[4])*OS[2]

for OC in OriginC:
    OC[3]=OC[3]/OC[2]#average number of seats for each month
    OC[4]=OC[2]/OC[1]
    OC[5]=(OC[3]*OC[4])*OC[2]

for DS in DestS:
    DS[3]=DS[3]/DS[2]#average number of seats for each month
    DS[4]=DS[2]/DS[1]
    DS[5]=(DS[3]*DS[4])*DS[2]

for DiRa in DistanceR:
    DiRa[3]=DiRa[3]/DiRa[2]#average number of seats for each month
    DiRa[4]=DiRa[2]/DiRa[1]
    DiRa[5]=(DiRa[3]*DiRa[4])*DiRa[2]

for DC in DestC:
    DC[3]=DC[3]/DC[2]#average number of seats for each month
    DC[4]=DC[2]/DC[1]
    DC[5]=(DC[3]*DC[4])*DC[2]

for AirT in AirCraft:
    AirT[3]=AirT[3]/AirT[2]#Average Number of Seats For Each Air Craft
    AirT[4]=AirT[2]/AirT[1]#Ratio Of how likely to complete a flight
    AirT[5]=(AirT[3]*AirT[4])*AirT[2]#Temp score of Avg seats * Ratio


for M in Months:
    data.loc[data.MONTH ==M[0], 'AVERAGE_SUCCESS_FOR_MONTH'] = M[4]#for every criteria with the same name as the first item in the list put the average number of sucesses for that criteria inside of the Data
    data.loc[data.MONTH ==M[0], 'OVERALL_RATING_FOR_MONTH'] = M[5]#for every criteria with the same name as the first item in the list put the number of sucesses for that criteria inside of the Data

for C in Carriers:
    data.loc[data.CARRIER_NAME ==C[0], 'AVERAGE_SUCCESS_FOR_CARRIER'] = C[4]
    data.loc[data.CARRIER_NAME ==C[0], 'OVERALL_RATING_FOR_CARRIER'] = C[5]

for OS in OriginS:
    data.loc[data.ORIGIN_STATE_NM ==OS[0], 'AVERAGE_SUCCESS_FOR_ORIGIN_STATE'] = OS[4]
    data.loc[data.ORIGIN_STATE_NM ==OS[0], 'OVERALL_RATING_FOR_ORIGIN_STATE'] = OS[5]

for OC in OriginC:
    data.loc[data.ORIGIN_CITY_NAME == OC[0], 'AVERAGE_SUCCESS_FOR_ORIGIN_CITY'] = OC[4]
    data.loc[data.ORIGIN_CITY_NAME == OC[0], 'OVERALL_RATING_FOR_ORIGIN_CITY'] = OC[5]

for DS in DestS:
    data.loc[data.DEST_STATE_NM == DS[0], 'AVERAGE_SUCCESS_FOR_DEST_STATE'] = DS[4]
    data.loc[data.DEST_STATE_NM == DS[0], 'OVERALL_RATING_FOR_DEST_STATE'] = DS[5]

for DiRa in DistanceR:
    data.loc[data.DISTANCE_RANGE == DiRa[0], 'AVERAGE_SUCCESS_FOR_DISTANCE'] = DiRa[4]
    data.loc[data.DISTANCE_RANGE == DiRa[0], 'OVERALL_RATING_FOR_DISTANCE'] = DiRa[5]

for DC in DestC:
    data.loc[data.DEST_CITY_NAME == DC[0], 'AVERAGE_SUCCESS_FOR_DEST_CITY'] = DC[4]
    data.loc[data.DEST_CITY_NAME == DC[0], 'OVERALL_RATING_FOR_DEST_CITY'] = DC[5]

for AirT in AirCraft:
    data.loc[data.AIRCRAFT_TYPE == AirT[0], 'AVERAGE_SUCCESS_FOR_AIR_CRAFT'] = AirT[4]
    data.loc[data.AIRCRAFT_TYPE == AirT[0], 'OVERALL_RATING_FOR_AIR_CRAFT'] = AirT[5]



Months=sorted(Months, key=operator.itemgetter(5), reverse=True)#sorts the score
Month=Months[0][0]#gets the top criteria
Month2=Months[1][0]
Month3=Months[2][0]

Carriers=sorted(Carriers, key=operator.itemgetter(5), reverse=True)
Car=Carriers[0][0]
Car2=Carriers[1][0]
Car3=Carriers[2][0]

DestS=sorted(DestS, key=operator.itemgetter(5), reverse=True)
DState=DestS[0][0]
DState2=DestS[1][0]
DState3=DestS[2][0]

DestC=sorted( DestC, key=operator.itemgetter(5), reverse=True)
DCity= DestC[0][0]
DCity2= DestC[1][0]
DCity3= DestC[2][0]

OriginC=sorted(OriginC, key=operator.itemgetter(5), reverse=True)
OCity=OriginC[0][0]
OCity2=OriginC[1][0]
OCity3=OriginC[2][0]

OriginS=sorted( OriginS, key=operator.itemgetter(5), reverse=True)
OState= OriginS[0][0]
OState2= OriginS[1][0]
OState3= OriginS[2][0]

DistanceR=sorted(DistanceR, key=operator.itemgetter(5), reverse=True)
DRange=DistanceR[0][0]
DRange2=DistanceR[1][0]
DRange3=DistanceR[2][0]

AirCraft=sorted(AirCraft, key=operator.itemgetter(5), reverse=True)
ACraft=AirCraft[0][0]
ACraft2=AirCraft[1][0]
ACraft3=AirCraft[2][0]

root = tk.Tk() #makes a tkinter object
root.geometry("200x100")# sets the size of the window
root.resizable(0, 0)# makes it unresizable
root.configure(background= "black")
root.option_add("*Button.Background","#d60415")
root.option_add("*Button.Foreground","#8c020e")
manual = tk.Button(root, text="Manual", command=create_Manual)# creates a manual button
manual.pack()
auto = tk.Button(root, text="Auto", command=create_Auto)# creates a auto button
auto.pack()
quitButton = tk.Button(root, text ='Exit', command=root.quit)
quitButton.pack()
#creates tkinter string variables so that they can be used for options
manVar1 = tk.StringVar()
manVar2 = tk.StringVar()
manVar3 = tk.StringVar()
manVar4 = tk.StringVar()
manVar5 = tk.StringVar()
manVar6 = tk.StringVar()

root.mainloop()
