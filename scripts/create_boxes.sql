create table if not exists Boxes
(
    ID INTEGER PRIMARY KEY AUTOINCREMENT
    , FriendlyName varchar(64)
    , DateCreated INTEGER -- POSIX timestamp use datetime.fromtimestamp(timestamp, tz='America/Los_Angeles')
    , DateClosed INTEGER -- POSIX timestamp use datetime.fromtimestamp(timestamp, tz='America/Los_Angeles')
    , IsOpen BOOLEAN -- 0 is open, 1 is closed
    , QRCode varchar(512) -- filepath to image-- pickled file. Use pickle to unpack  use pip install qrcode to generate
    , PhysicalLocation varchar(512)
)