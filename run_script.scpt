-- # osascript -e "tell application \"Adobe Photoshop CC 2017\" do javascript \"#include $1\""

-- on run argv
    -- set photoshopTarget to item 1 of argv
-- set photoshopTarget to "Adobe Photoshop CC 2017"
-- set jsFile to item 2 of argv

-- tell application photoshopTarget
--     with timeout of 3600 seconds
--         activate
--         set jsFile to item 1 of argv
--         set jsFile to <full_path>/<script.jsx>
        
--         do javascript of file jsFile
--         set js to "
--         #include '" & jsFile & "';
--         " & "main();"

--         do javascript "alert('test');"
--     end timeout
-- end tell

-- end run