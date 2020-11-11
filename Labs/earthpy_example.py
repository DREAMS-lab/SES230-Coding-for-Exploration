import os
from glob import glob
import matplotlib.pyplot as plt
import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep
from matplotlib import colors


data = et.data.get_data("vignette-landsat")
os.chdir(os.path.join(et.io.HOME, "earth-analytics"))

# Stack the Landsat 8 bands
# This creates a numpy array with each "layer" representing a single band
# You can use the nodata= parameter to mask nodata values
landsat_path = glob(
    os.path.join(
        "data",
        "vignette-landsat",
        "LC08_L1TP_034032_20160621_20170221_01_T1_sr_band*_crop.tif",
    )
)
landsat_path.sort()
array_stack, meta_data = es.stack(landsat_path, nodata=-9999)

titles = ["Ultra Blue", "Blue", "Green", "Red", "NIR", "SWIR 1", "SWIR 2"]
# sphinx_gallery_thumbnail_number = 1
# ep.plot_bands(array_stack, title=titles)
# plt.show()

falsecolor = [array_stack[4], array_stack[1], array_stack[2]]
plt.imshow(falsecolor)
# plt.colorbar()
plt.show()

