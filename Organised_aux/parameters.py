###PARAMETERS---------------------------------------------------------------------
###


#Independent of iterated values--ln and ln2-------------------------------------------------------------------------
#the hinge width
ln2=2.0E-3
#edge length of a square
l=50.0E-3
'''ln1 and ln will be changed as a function of theta'''

theta_list=np.arange(1,45.5,0.5).tolist()


#ln=50.0

##number of unit cells-----------------------------
nx=2        #number of unit cells x direction
ny=2         #number of unit cells in y direction

##geometry counter
ctr=1

##displacement at right boundary
right_disp=20E-3

#Material properties-----------------------------------------------
Ex=200E9  #youngs modulus of the material used
v=0.29   #poissons ratio of the materials used
rho=7872
#Mesh Constraints
mesh_size=1.0E-3

theta_poi_dict={}
theta_poi_dict_m={}
number_till=4