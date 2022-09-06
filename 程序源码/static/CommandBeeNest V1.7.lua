function Menu()
    local menu = [[
    {
      "type": "form",
      "title": "§6菜单",
      "content": "§e请选择需要执行的操作",
      "buttons": [
        {
          "text": "§7自定义命令"
        },
        {
          "text": "§7选择玩家"
        },
        {
          "text": "§7修改选项"
        },
        {
          "text": "§c退出脚本"
        }
      ]
    }
    ]]
    addForm(menu, function(index)
        if (index == 0) then
            Command()
        end
        if (index == 1) then
            ChoosePlayer()
        end
        if (index == 2) then
            Setting()
        end
        if (index == 3) then
            clientMessage('§7[命令蜂巢] §e脚本已关闭')
            exit()
        end
    end)
end

function Command()
    local menu = [[
       {
          "type": "custom_form",
          "title": "§b自定义命令",
          "content": [
            {
              "type": "input",
              "placeholder": "gamemode 1 @a",
              "text": "指令"
            }
          ]
        }
    ]]
    addForm(menu, function(Command)

        if Command == -1 then
            Success = true
            Menu()
        end

        if Success ~= true then
            GetCommand(Command, Command, "Command")
        end
    end)
end

function ChoosePlayer()
    list = getWorldPlayerList()
    id = getLocalPlayerUniqueID()
    name = getEntityName(id)
    local menu = {
        type = 'form',
        title = '选择玩家',
        content = '请选择需要执行的玩家',
        buttons = { { text = '暂无数据' } }
    }
    if #list > 0 and list then
        for i = 1, #list do
            jsonz = list[i].name
            menu.buttons[1] = { text = '全部玩家' }
            menu.buttons[i + 1] = { text = jsonz }
        end
    end
    addForm(dkjson.encode(menu, {}), function(index)
        if index >= 0 then
            if index == 0 then
                AllPlayer()
            else
                Index = index
                OnlyPlayer()
            end
        else
            Menu()
        end
    end)
end

function AllPlayer()
    local menu = [[
    {
      "type": "form",
      "title": "§a命令选择",
      "content": "§e请选择需要执行的操作",
      "buttons": [
        {
          "text": "§b踢出"
        },
        {
          "text": "§b清包"
        },
        {
          "text": "§b创造"
        },
        {
          "text": "§b生存"
        },
        {
          "text": "§b冒险"
        },
        {
          "text": "§b雷电"
        }
      ]
    }
    ]]
    addForm(menu, function(Operate)
        if (Operate == 0) then
            NBT = ""
            for i = 1, #list do
                if list[i].id ~= id then
                    if i ~= #list then
                        NBT = NBT .. '{ActorIdentifier:"minecraft:command_block_minecart<>",SaveData:{Persistent:1b,Ticking:1b,definitions:["+minecraft:bee"],Command:"kick "' .. list[i].name .. '" ' .. Reason .. '",modelName:"ty_yuanshenghuli_0_0"},TicksLeftToStay:0},'
                    else
                        NBT = NBT .. '{ActorIdentifier:"minecraft:command_block_minecart<>",SaveData:{Persistent:1b,Ticking:1b,definitions:["+minecraft:bee"],Command:"kick "' .. list[i].name .. '" ' .. Reason .. '",modelName:"ty_yuanshenghuli_0_0"},TicksLeftToStay:0}'
                    end
                end
            end
            clientMessage("§b[命令蜂巢] §e请打开锻造台后等待" .. math.ceil(Delay) .. "秒")
            function onPlayerBuildBlockEvent(PlayerId, x, y, z, side)
                local Block = getBlock(x, y, z)
                if Block.namespace == "minecraft:smithing_table" then
                    thread(function()
                        if UseBeeNest == true then
                            addInventoryItemByNBT('{Block:{name:"minecraft:movingBlock",states:{},val:0s,version:17879555},Count:64b,Damage:0s,Name:"minecraft:movingblock",WasPickedUp:0b,tag:{display:{Lore:["§r§l§b' .. Reason .. '§r"],Name:"§r§l§eGanRen BeeNest KickAll"},movingBlock:{name:"minecraft:bee_nest"},movingEntity:{Occupants:[' .. NBT .. '],id:"Beehive"},KeepOnDeath:1b}}')
                        else
                            addInventoryItemByNBT('{Block:{name:"minecraft:movingBlock",states:{},val:0s,version:17879555},Count:64b,Damage:0s,Name:"minecraft:movingblock",WasPickedUp:0b,tag:{display:{Lore:["§r§l§b' .. Reason .. '§r"],Name:"§r§l§eGanRen Air KickAll"},movingBlock:{name:"minecraft:air"},movingEntity:{Occupants:[' .. NBT .. '],id:"Beehive"},KeepOnDeath:1b}}')
                        end
                        clientMessage("§b[命令蜂巢] §e已成功获取")
                        function onPlayerBuildBlockEvent(PlayerId, x, y, z, side)
                        end
                    end, Delay * 1000)
                else
                    clientMessage('§b[命令蜂巢] §e请打开锻造台或退出脚本')
                    return true
                end
            end
        end
        if (Operate == 1) then
            GetCommand("clear @a[name=!\"" .. name .. "\"]", "clear @a[name=!\"" .. name .. "\"]", "ClearAll")
        end
        if (Operate == 2) then
            GetCommand("gamemode c @a", "gamemode c @a", "CreateAll")
        end
        if (Operate == 3) then
            GetCommand("gamemode s @a[name=!\"" .. name .. "\"]", "gamemode s @a[name=!\"" .. name .. "\"]", "SurviveAll")
        end
        if (Operate == 4) then
            GetCommand("gamemode a @a[name=!\"" .. name .. "\"]", "gamemode a @a[name=!\"" .. name .. "\"]", "AdventureAll")
        end
        if (Operate == 5) then
            GetCommand("execute @a[name=!\"" .. name .. "\"]~~~summon lightning_bolt", "execute @a[name=!\"" .. name .. "\"]~~~summon lightning_bolt", "LightningAll")
        end
        if (Operate < 0) then
            ChoosePlayer()
        end
    end)
end

function OnlyPlayer()
    local menu = [[
    {
      "type": "form",
      "title": "§6命令选择",
      "content": "§e请选择需要执行的操作",
      "buttons": [
        {
          "text": "§7踢出"
        },
        {
          "text": "§7清包"
        },
        {
          "text": "§7创造"
        },
        {
          "text": "§7生存"
        },
        {
          "text": "§7冒险"
        },
        {
          "text": "§7雷电"
        },
        {
          "text": "§7自定义指令"
        }
      ]
    }
    ]]
    addForm(menu, function(Operate)
        if (Operate == 0) then
            GetCommand("kick \"" .. list[Index].name .. "\" " .. Reason, "kick \"" .. list[Index].name .. "\" " .. Reason, "Command")
        end
        if (Operate == 1) then
            GetCommand("clear \"" .. list[Index].name .. "\"", "clear \"" .. list[Index].name .. "\"", "Command")
        end
        if (Operate == 2) then
            GetCommand("gamemode 1 \"" .. list[Index].name .. "\"", "gamemode 1 \"" .. list[Index].name .. "\"", "Command")
        end
        if (Operate == 3) then
            GetCommand("gamemode 0 \"" .. list[Index].name .. "\"", "gamemode 0 \"" .. list[Index].name .. "\"", "Command")
        end
        if (Operate == 4) then
            GetCommand("gamemode 2 \"" .. list[Index].name .. "\"", "gamemode 2 \"" .. list[Index].name .. "\"", "Command")
        end
        if (Operate == 5) then
            GetCommand("execute \"" .. list[Index].name .. "\"~~~summon lightning_bolt", "execute \"" .. list[Index].name .. "\"~~~summon lightning_bolt", "Command")
        end
        if (Operate == 6) then
            Variable()
        end
        if (Operate < 0) then
            ChoosePlayer()
        end
    end)
end

function Variable()
    local menu = [[
       {
          "type": "custom_form",
          "title": "§7自定义命令",
          "content": [
            {
              "type": "input",
              "placeholder": "支持变量 [Player]",
              "text": "指令"
            }
          ]
        }
    ]]
    addForm(menu, function(Cmd)
        if Cmd == -1 then
            OnlyPlayer()
        else
            local Cmd = string.gsub(Cmd, "%[Player]", list[Index].name)
            GetCommand(Cmd, Cmd, "Command")
        end
    end)
end

function Setting()
    local menu = string.format('{"type":"custom_form","title":"§b设置","content":[{"type":"slider","text":"等待时间(秒)","min":0,"max":60,"step":1,"default":%d},{"type":"toggle","text":"使用蜂巢","default":%s},{"type":"input","text":"踢出原因","default":%q}]}', Delay, bool2jsonValue(UseBeeNest), Reason)
    addForm(menu, function(Time, BeeNest, reason)
        if Time == -1 then
            Time = 0
        end
        UseBeeNest = BeeNest
        Delay = Time
        Reason = reason
        Menu()
    end)
end

function GetCommand(Command, Lore, Name)
    clientMessage("§b[命令蜂巢] §e请打开锻造台后等待" .. math.ceil(Delay) .. "秒")
    function onPlayerBuildBlockEvent(PlayerId, x, y, z, side)
        local Block = getBlock(x, y, z)
        if Block.namespace == "minecraft:smithing_table" then
            thread(function()
                if UseBeeNest == true then
                    addInventoryItemByNBT('{Block:{name:"minecraft:movingBlock",states:{},val:0s,version:17879555},Count:64b,Damage:0s,Name:"minecraft:movingblock",WasPickedUp:0b,tag:{display:{Lore:["§r§l§b' .. Lore .. '§r"],Name:"§r§l§eGanRen BeeNest ' .. Name .. '"},movingBlock:{name:"minecraft:bee_nest"},movingEntity:{Occupants:[{ActorIdentifier:"minecraft:command_block_minecart<>",SaveData:{Persistent:1b,Ticking:1b,definitions:["+minecraft:bee"],Command:"' .. Command .. '",modelName:"ty_yuanshenghuli_0_0"},TicksLeftToStay:0}],id:"Beehive"},KeepOnDeath:1b}}')
                else
                    addInventoryItemByNBT('{Block:{name:"minecraft:movingBlock",states:{},val:0s,version:17879555},Count:64b,Damage:0s,Name:"minecraft:movingblock",WasPickedUp:0b,tag:{display:{Lore:["§r§l§b' .. Lore .. '§r"],Name:"§r§l§eGanRen Air ' .. Name .. '"},movingBlock:{name:"minecraft:air"},movingEntity:{Occupants:[{ActorIdentifier:"minecraft:command_block_minecart<>",SaveData:{Persistent:1b,Ticking:1b,definitions:["+minecraft:bee"],Command:"' .. Command .. '",modelName:"ty_yuanshenghuli_0_0"},TicksLeftToStay:0}],id:"Beehive"},KeepOnDeath:1b}}')
                end
                clientMessage("§b[命令蜂巢] §e已成功获取")
                function onPlayerBuildBlockEvent(PlayerId, x, y, z, side)
                end
            end, Delay * 1000)
        else
            clientMessage('§b[命令蜂巢] §e请打开锻造台或退出脚本')
            return true
        end
    end
end

function onSendChatMessageEvent(message)
    if message == '菜单' then
        Menu()
        clientMessage("§b[命令蜂巢] §e菜单已开启")
        return true;
    end
end

function Error(data)
    clientMessage("§cError:" .. data)
end

function bool2jsonValue(bool)
    if bool then
        return 'true'
    else
        return 'false'
    end
end

dkjson = require("dkjson")
UseBeeNest = false
Delay = 0
Reason = "You are loser By TestStudio-GanRen"
Version = "V1.7"
clientMessage('§e命令蜂巢' .. Version .. '\n§b[命令蜂巢] §e脚本加载完成，聊天框输入"菜单"来唤起\n§b[命令蜂巢] §e作者:GanRen QQ:2950347657')
Menu()