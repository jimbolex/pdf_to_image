from pdf2image import convert_from_path, convert_from_bytes

# Convert PDF to images
images = convert_from_path('Canada_Scan_App_Issue_Timeline.pdf')

# Save each page as an image
for i in range(len(images)):
    images[i].save('page' + str(i) + '.jpg', 'JPEG')