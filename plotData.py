#Smart and Fermi-LAT data

import numpy as np
import numpy
import matplotlib.pyplot as plt


#Fermi-LAT data



f1 = open('/media/david/E/Swift/4c/plotdata/lightCurve_result_activity2_3days.txt').read()


Tmin_MET, Tmax_MET, Flux, Flux_err, Index, Index_err, TS = np.loadtxt('lightCurve_result_activity2_3days.txt', skiprows=0, unpack=True)
Tmid_MET=(Tmin_MET+Tmax_MET)/2

Tmin_MJD=Tmin_MET/86400+51910
Tmid_MJD=Tmid_MET/86400+51910
Tmax_MJD=Tmax_MET/86400+51910

FGscale=10**7
Flux=FGscale*Flux
#print max(Flux)
Flux_err=FGscale*Flux_err

#f2 = open('/media/david/9C0CA8EF0CA8C59C/Codes/PlotData/swift_xrt_flux.txt').read()
#Sequence, Tmid_mjd_Swift, Flux_SwiftXrt, Flux_err_Swift_Xrt = np.loadtxt('swift_xrt_flux.txt', skiprows=0, unpack=True)

#FluxXRT=10**12*10**(Flux_SwiftXrt) 

#Fmin=10**(FluxXRT-Flux_err_Swift_Xrt)
#Fmax=10**(FluxXRT+Flux_err_Swift_Xrt)

#FluxXRT_err= (((FluxXRT-Fmin)**2 + (FluxXRT-Fmax)**2)/2) ** 0.5

fig, axes = plt.subplots(2,sharex=True)
axes[0].errorbar(Tmid_MJD, Flux, yerr=Flux_err, xerr=3.5, fmt='o', color='black', ecolor='black',ms=3,capsize=0)
axes[0].set_title('lightCurve Result activity_2 and bin size=3 day')
axes[0].set_ylabel('F (10^-7 ph cm^-2 s^-1)')
axes[0].axis([57680,58484,0,20])
#Swift lines
#axes[0].errorbar(Tmid_mjd_Swift, Flux_SwiftXrt, yerr=1000, xerr=0, fmt='o', color='Blue', ecolor='blue',ms=0.1,capsize=0)

#Swift XRT Flux
#axes[1].errorbar(Tmid_mjd_Swift, FluxXRT, yerr=Flux_err_Swift_Xrt, xerr=0, fmt='o', color='Red', ecolor='Red',ms=3,capsize=0)
#axes[1].set_title('')
#axes[1].set_ylabel('F (10^-12 erg cm^-2 s^-1)')
#axes[1].axis([54500,58600,-1,11])

#TS vs Flux
axes[1].errorbar(Tmid_MJD, TS, yerr=0, xerr=3.5, fmt='o', color='green', ecolor='green',ms=3,capsize=0)
#axes[1].set_title('TS vs Flux')
axes[1].set_ylabel('TS')
axes[1].set_xlabel('Time (MJD)')
axes[1].axis([57680,58484,0,2000])

#axes[1].errorbar(MJD_B, FlambdaB, FlambdaVerr, fmt='o', color='blue', ecolor='blue',ms=3,capsize=0)
#axes[1].set_ylabel('B(mJy)')
#axes[1].axis([min(Tmid_MJD)-20,max(Tmid_MJD)+20,min(FlambdaB)-1,max(FlambdaB)+1])
#axes[2].errorbar(MJD_V, FlambdaV, FlambdaVerr, fmt='o', color='red', ecolor='red',ms=3,capsize=0)
#axes[2].set_ylabel('V(mJy)')
#axes[2].axis([min(Tmid_MJD)-20,max(Tmid_MJD)+20,min(FlambdaV)-4,max(FlambdaV)+4])
#axes[3].errorbar(MJD_R, FlambdaR, FlambdaRerr, fmt='o', color='Magenta', ecolor='Magenta',ms=3,capsize=0)
#axes[3].set_ylabel('R(mJy)')
#axes[3].axis([min(Tmid_MJD)-20,max(Tmid_MJD)+20,min(FlambdaR)-4,max(FlambdaR)+4])
#axes[4].errorbar(MJD_J, FlambdaJ, FlambdaJerr, fmt='o', color='g', ecolor='g',ms=3,capsize=0)
#axes[4].set_ylabel('J(mJy)')
#axes[4].axis([min(Tmid_MJD)-20,max(Tmid_MJD)+20,min(FlambdaJ)-4,max(FlambdaJ)+4])
#axes[5].errorbar(MJD_K, FlambdaK, FlambdaKerr, fmt='o', color='cyan', ecolor='cyan',ms=3,capsize=0)
#axes[5].set_ylabel('K (mJy)')
#axes[5].set_xlabel('Time (MJD)')
#axes[5].axis([min(Tmid_MJD)-20,max(Tmid_MJD)+20,min(FlambdaK)-10,max(FlambdaK)+10])
plt.subplots_adjust(left=0.055, bottom=0.06, right=0.99, top=0.94, hspace=0)
plt.show() 

