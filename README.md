### EAN Look-Up

## The Problem
Staff in the company I work for needed a way to scan a barcode and load up a photo of the product. This assists packing by allowing the packer to scan the product barcode and visually confirm the item is correct. This also speeds up Exchanges and returns by displaying siblong products of differing sizes.

## The Solution
Linnworks Order Management out puts a CSV file of all currently stocked products. We also have a media folder containing 6 images of each product stored in colders named after the product SKU.
The CSV file contains both the SKU and the EAN in th form of a scannable barcode. The product SKU does not have a barcode.

Using Tkinter to create a basic GUI with a Search box, we accept the barcode from the scanner into the box and search the media folder for the correct product photo folder. Then we load the first image and display it for the user.

To Do: Implement a way to match mulitple colour ways
