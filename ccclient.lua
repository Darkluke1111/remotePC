cb = peripheral.find("chatBox")
local connectionURL = "ws://85.214.150.226:8765"
local ws, err = http.websocket(connectionURL)
if not ws then
  return printError(err)
end

ws.send("Hello world!")



function receive()
    while true do
        local _, url, response, isBinary = os.pullEvent("websocket_message")

        -- We need this if statement to check that we received the message from
        -- the correct websocket. After all, you can have many websockets connected to
        -- different URLs.
        if url == connectionURL then
            print(response)
            cb.sendMessage(response,"LukeBot")
        end  
    end
end

function send()
    while true do
        local _, username, message = os.pullEvent("chat")
        --ws.send(username .. ": " .. message)
    end
end

parallel.waitForAny(receive,send)