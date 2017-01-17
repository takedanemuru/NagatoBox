### Cache Directory

CoverArtFile : `$XDG_CACHE_HOME/nagato-player-x`

### Database

Host : `$XDG_DATA_HOME/NagatoBox/database/Media`

#### Tables

##### NagatoTableLibrary

Column		|DataType	|Note
----		|----		|----
id		|integer		|PrimaryKey
title		|string		|-
artist		|string		|-
album		|string		|-
path		|string		|full path of each music file
duration		|float		|in seconds

##### NagatoTablePlaylistNames

Column		|DataType	|Note
----		|----		|----
id		|integer		|PrimaryKey
playlist_name	|string		|-
playlist_description	|string		|-


##### NagatoTablePlaylistData

Column		|DataType	|Note
----		|----		|----
id		|integer		|PrimaryKey
playlist_name_id	|integer		|( TablePlaylistNames.id )
path		|string		|fullpath of each music file

