from pysheeter.PySheeter import Sheet

# Load sprites from './files/' (all sprites are 64x64)
spritesheet = PySheeter.Sheet("example/files")

# Create a vertical spritesheet with the dimensions 16x16 (scaled)
spritesheet.put("example_v1616.png",(16,16))
