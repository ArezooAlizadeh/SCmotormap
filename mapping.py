import numpy as np

def affmapping(R, phi, A=5.3, Bu=1.8, Bv=1.8):
	'''
	Afferent mapping from visual field to the collicular surface.

	See:
	Ottes, F. P., Van Gisbergen, J. A. M., & Eggermont, J. J. (1986).
		Visuomotor fields of the superior colliculus: a quantitative model.
		Vision Research, 26(6), 857-873.
		
	Input arguments:
	R (deg), phi (deg), A (deg), Bu (mm), Bv (mm/deg)

	Returns:
	u (mm), v (mm)
	'''
	degphi = np.pi*phi/180
	u = Bu*np.log2(np.sqrt(R**2+A**2+2*A*R*np.cos(degphi))/A)
	v = Bv*np.arctan((R*np.sin(degphi))/(R*np.cos(degphi)+A))
	return u, v



def effmapping(u, v, eta=1, A=5.3, Bu=1.8, Bv=1.8):
	'''
	Efferent mapping for horizontal and vertical components of location dependent mini-vectors.

	See:
	Van Opstal, A. J., & Goossens, H. H. L. M. (2008).
	Linear ensemble-coding in midbrain superior colliculus specifies the saccade kinematics.
	Biological Cybernetics, 98(6), 561-77.

	Input arguments:
	u (mm), v (mm), eta (scaling factor), A (deg), Bu (mm), Bv (mm/deg)

	Returns:
	x, y
	'''
	x = eta*A*np.exp(u/Bu)*np.cos(v/Bv)-1
	y = eta*A*np.exp(u/Bu)*np.sin(v/Bv)
	return x, y
