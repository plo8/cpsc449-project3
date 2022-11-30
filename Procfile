auth: hypercorn auth --reload --debug --bind auth.local.gd:$PORT --access-logfile - --error-logfile - --log-level DEBUG
game_1: hypercorn game --reload --debug --bind game.local.gd:$PORT --access-logfile - --error-logfile - --log-level DEBUG
game_2: hypercorn game --reload --debug --bind game.local.gd:$PORT --access-logfile - --error-logfile - --log-level DEBUG
game_3: hypercorn game --reload --debug --bind game.local.gd:$PORT --access-logfile - --error-logfile - --log-level DEBUG
primary: ./bin/litefs-v0.2.0-linux-amd64/litefs -config ./etc/primary.yml
secondary: ./bin/litefs-v0.2.0-linux-amd64/litefs -config ./etc/secondary.yml
secondary_other: ./bin/litefs-v0.2.0-linux-amd64/litefs -config ./etc/secondary_other.yml