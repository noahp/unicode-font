# unicode-font

This badly named tool will do character substitution to get fancy text you can
shove into places that don't have actual font support.

Also known as twitter font generator, or unicode font generator/converter.

```bash
❯ python unicode-font.py --list-fonts --ignore-case
aesthetic : ｌｏｒｕｍ　ｉｐｓｕｍ　０１２３４
bold : 𝐥𝐨𝐫𝐮𝐦 𝐢𝐩𝐬𝐮𝐦 𝟎𝟏𝟐𝟑𝟒
bold-italic : 𝙡𝙤𝙧𝙪𝙢 𝙞𝙥𝙨𝙪𝙢 01234
bold-script : 𝓵𝓸𝓻𝓾𝓶 𝓲𝓹𝓼𝓾𝓶 01234
bubble : ⓛⓞⓡⓤⓜ ⓘⓟⓢⓤⓜ ⓪①②③④
bubble-negative : 🅛🅞🅡🅤🅜 🅘🅟🅢🅤🅜 ⓿➊➋➌➍
double-struck : 𝕝𝕠𝕣𝕦𝕞 𝕚𝕡𝕤𝕦𝕞 𝟘𝟙𝟚𝟛𝟜
emoji : 👢⚽🌱⛎〽️ 🎐🅿️💲⛎〽️ 01234
italic : 𝘭𝘰𝘳𝘶𝘮 𝘪𝘱𝘴𝘶𝘮 01234
script : 𝓁𝑜𝓇𝓊𝓂 𝒾𝓅𝓈𝓊𝓂 01234
small-capital : ʟᴏʀᴜᴍ ɪᴘsᴜᴍ 01234
square : 🄻🄾🅁🅄🄼 🄸🄿🅂🅄🄼 01234
square-negative : 🅻🅾🆁🆄🅼 🅸🅿🆂🆄🅼 01234
strike : l̶o̶r̶u̶m̶ i̶p̶s̶u̶m̶ 0̶1̶2̶3̶4̶
tilde-strike : l̴o̴r̴u̴m̴ i̴p̴s̴u̴m̴ 0̴1̴2̴3̴4̴
underline : l̲o̲r̲u̲m̲ i̲p̲s̲u̲m̲ 0̲1̲2̲3̲4̲
upsidedown : ˥oɹnɯ ᴉdsnɯ 0ƖᄅƐㄣ
```

Character mappings were taken from here and tweaked a tiny bit:

- https://raw.githubusercontent.com/santillan/textgenerator/master/includes/json/character-sets.json
- https://raw.githubusercontent.com/chreeonyx/www.chree.ga/c0ed1fefb22a155b7c05c68015ab099235febaec/bot/lib/fonts.py
