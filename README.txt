objective:
track paperwork so I don't have to manually

inject flow:
scan box
scan page
upload to blob storage
scan text and store in text
categorize?


databases needed:
Documents:
    ID
    DateUploaded
    Image
    PageNumber
    BoxID
    Sender
    Category
    Notes

Boxes:
    ID
    FriendlyName
    DateCreated
    DateClosed
    IsOpen
    QRCode
    PhysicalLocation