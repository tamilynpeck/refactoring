# Gilded Rose Kata

https://kata-log.rocks/gilded-rose-kata

https://github.com/emilybache/GildedRose-Refactoring-Kata

# Introduction

- All items have a SellIn value which denotes the number of days we have to sell the item
- All items have a Quality value which denotes how valuable the item is
- At the end of each day our system lowers both values for every item
- Once the sell by date has passed, Quality degrades twice as fast
- The Quality of an item is never negative
- The Quality of an item is never more than 50
- “Aged Brie” actually increases in Quality the older it gets
- “Sulfuras”, being a legendary item, never has to be sold or decreases in Quality
  - “Sulfuras” is a legendary item and as such its Quality is 80 and it never alters.
- “Backstage passes”, increases in Quality as its SellIn value approaches;
  - Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
  - Quality drops to 0 after the concert

# Your Task

We have recently signed a supplier of conjured items. This requires an update to our system:

“Conjured” items degrade in Quality twice as fast as normal items

# Rules

Feel free to make any changes to the UpdateQuality method and add any new code as long as everything still works correctly.
However, do not alter the Item class or Items property (you can make the UpdateQuality method and Items property static if you like).
