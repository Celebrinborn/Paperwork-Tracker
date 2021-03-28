create table if not exists Documents
(
    ID INTEGER PRIMARY KEY AUTOINCREMENT
    , DateUploaded INTEGER -- POSIX timestamp use datetime.fromtimestamp(timestamp, tz='America/Los_Angeles')
    , Image varchar(512) -- filepath to image
    , PageNumber INTEGER
    , BoxID INTEGER
    , Sender varchar(512)
    , Category varchar(512)
    , Notes varchar(2048)

    , FOREIGN KEY(BoxID) REFERENCES Boxes(ID)
)