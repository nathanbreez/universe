### Configuration & Environment
> Note :
>> for sample-string.env, you just need to rename it or create a new one to be string.env and save it.
>>> for sample-configuration.py u must be create new or copy file. Don't rename file!!!

### For Description
> Note :
>> For details, have a look and read at sample-string.env and sample-configuration.py, we have provided descriptions on each of the environments and configuration.

### Get Telehon String ›_

```sh
# clone repository
git clone https://github.com/unknownkz/universe

# change directory
cd universe/universe/Configuration

# execute program [ to get string ]
python3 -m telethon_string

# Don't forget to fill your api id, api hash and phone number in string.env
# see sample-string.env
```

### Example Filling Configuration
<kbd> Create a new file with the name configuration.py </kbd>
<kbd> ( Don't rename file from sample ) </kbd>
```python
### Required for Telegram Api
# get it at my.telegram.org | api development tools | then fill
Api_ID = int(then_get("Api_ID", "182838181")) # <- fill in here " "
Api_Hash = str(then_get("Api_Hash", "57c7822bw02dE")) # <- fill in here " "

### Logger Information
# add @MissRose_Bot to ur chat and write /id to get ur chat id
Logger_ID = then_get("Logger_ID", "-10083828272") # <- fill here " "
# Go to @BotFather on Telegram, type /newbots | then follow the steps | If finished then take the Bot Token.
Token_Bot = str(then_get("Token_Bot", "173637:H7joKL28483")) # <- fill here " "
```
<kbd> Don't forget to add your bot to the group. </kbd>
