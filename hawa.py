import base64

# Read the GLB file and encode it as a base64 string
with open('model.glb', 'rb') as file:
    glb_content = file.read()
    glb_base64 = base64.b64encode(glb_content).decode('utf-8')

# Print the base64 string
print(glb_base64)
