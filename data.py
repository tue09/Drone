number_customer=20
number_truck=3
number_drone=3
speed_truck=30
speed_drone=45
capacity_drone=3
Max_Drone_Flight_Time=1
Drone_Unloading_Time=5/60
file_object=open("C:\\Users\\ADMIN\\Downloads\\TSPrd(time)\\Solomon\\20\\C101_2.5.dat")
data=file_object.readlines()
coordinates=[0]*(number_customer+1)
for i in range(0,len(coordinates)):
    coordinates[i]=[]
time_release=[0]*(number_customer+1)
for i in range(0,number_customer+1):
    u=list(data[i+5])
    x=[]
    for j in range(0,len(u)):
        if u[j]=='\t'and u[j-1]!='\t':
            x.append(j)
    for j in range(len(u)-1,0):
        if u[j]=="\t":
            x.append(j)
            break
    coordinates[i].append(int(data[i+5][0:x[0]]))
    coordinates[i].append(int(data[i+5][x[0]+1:x[1]]))
    time_release[i]=int(data[i+5][x[len(x)-1]+1:len(data[i+5])-1])
class cus:
    def __init__(self, coordinates,release_date,weight):
        self.coordinates = coordinates
        self.release_date=release_date/60
        self.weight=weight
depot=coordinates[0]
customer=[0]*(number_customer+1)
customer[0]=cus(coordinates[0],0,0)
for i in range(1,len(customer)):
    customer[i]=cus(coordinates[i],time_release[i],1)
truck_path_array=[1,11,20,5,7,14,0,2,4,6,16,10,3,13,15,0,9,18,19,12,17,8]
x=[0.4,0.45,0.2,0.6,0.9,0.1,0.4,0.6,0.85,0.9,0.15,0.65,0.25,0.05,0.075,0.8,0.8,0.3,0.22,0.1,0.1,0.4]
#