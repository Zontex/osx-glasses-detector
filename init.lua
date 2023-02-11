function caffeinateWatcher(eventType)
    if (eventType == hs.caffeinate.watcher.systemDidWake) then
            print ("Woken...")
            -- Execute wake script
            hs.task.new("/Users/your_username_goes_here/.wakeup", nil):start()
    end
end

sleepWatcher = hs.caffeinate.watcher.new(caffeinateWatcher)
sleepWatcher:start()