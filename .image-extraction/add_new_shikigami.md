# Adding new Shikigami

Remove all current images:

fd -e png -x rm {}

After convert, copy to the character folder in assets:

fd -e png kuro_shiro_mujou -x mv {} /Users/dtomlinson/git-repos/web-dev/onmyoji-deck-builder/src/assets/cards/kuro_shiro_mujou

Print all cards (excluding char and avatar):

fd -E '*char*' -E '*avatar*' | wc && fd -E '*char*' -E '*avatar*'

Blank JSON template:

- Paste template in
- Fill in with new char name
- Fill in filenames
- Copy `cards`
- Select all items in `cards`
- New line and paste to duplicate
- Update GUID

```json
  {
    "name": "kuro_shiro_mujou",
    "character_card": "kuro_shiro_mujou/kuro_shiro_mujou-char.png",
    "cards": [
      { "id": "d6fc26b2", "name": "", "url": "" },
      { "id": "1217f957", "name": "", "url": "" },
      { "id": "a507638d", "name": "", "url": "" },
      { "id": "a3e876ec", "name": "", "url": "" },
      { "id": "8fa65d84", "name": "", "url": "" },
      { "id": "914c6cbb", "name": "", "url": "" },
      { "id": "f1f8ce7d", "name": "", "url": "" },
      { "id": "1d30d350", "name": "", "url": "" },
    ],
    "avatar": "kuro_shiro_mujou/kuro_shiro_mujou-avatar.png"
  }
```
