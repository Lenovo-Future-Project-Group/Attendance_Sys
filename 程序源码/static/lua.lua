BASE_PATH = getResource()
list = file_list(BASE_PATH .. "/script")
luas = "1"
luas = getData("lua", luas)

if luas ~= "1" then
    listall = '{"text":"§2上次执行LUA:' .. luas .. '"}'
else
    listall = '{"text":"§4最近未执行LUA"}'
end

for i = 1, #list do
    jsonz = list[i].name
    if jsonz ~= "base.lua" and jsonz ~= "dkjson.lua" and jsonz ~= "lua.lua" and jsonz ~= "docs.md" and jsonz ~= "main.lua" then

        listall = listall .. ',{"text":"§b' .. jsonz .. '"}'
    else
        listall = listall .. ',{"text":"§a[基础]' .. jsonz .. '"}'
    end


end
local id = tostring(getLocalPlayerUniqueID())
local item = getEntityCarriedItem(id)
local json = string.format('{"type":"form","title":"§6快捷执行Lua","content":"§7我的实体ID:' .. id .. '| 当前手持物品ID:' .. item.id .. '[' .. item.namespace .. ']","buttons":[' .. listall .. ']}')

addForm(json, function(index)

    if index ~= -1 then
        if index == 0 then
            clientMessage("§7执行LUA->§e" .. luas)
            loadLua(luas)
        else
            clientMessage("§7执行LUA->§e" .. list[index].name)
            loadLua(list[index].name)
            setData("lua", list[index].name)
        end
    end


end)