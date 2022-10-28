import pytest
from gilded_rose import Item, GildedRose


def test_foo():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert "foo" == items[0].name


def test_regular_items_decrease_by_one():
    gilded_rose = GildedRose([Item("+5 Dexterity Vest", 10, 20)])
    expected = {"sell_in": 9, "quality": 19}

    gilded_rose.update_quality()

    item = gilded_rose.items[0]
    assert item.quality == expected["quality"]
    assert item.sell_in == expected["sell_in"]


def test_quality_goes_up_for_improving_products():
    gilded_rose = GildedRose(
        [
            Item("Aged Brie", 20, 30),
            Item("Backstage passes to a TAFKAL80ETC concert", 20, 30),
        ]
    )
    expected = [
        {"sell_in": 19, "quality": 31},
        {"sell_in": 19, "quality": 31},
    ]

    gilded_rose.update_quality()

    for index, expectation in enumerate(expected):
        item = gilded_rose.items[index]
        assert item.quality == expectation["quality"]
        assert item.sell_in == expectation["sell_in"]


def test_quality_goes_up_by_two_for_backstage_passes_with_10_days_or_less_left():
    gilded_rose = GildedRose(
        [
            Item("Backstage passes to a TAFKAL80ETC concert", 8, 30),
        ]
    )
    expected = {"sell_in": 7, "quality": 32}

    gilded_rose.update_quality()

    item = gilded_rose.items[0]
    assert item.quality == expected["quality"]
    assert item.sell_in == expected["sell_in"]


def test_quality_goes_up_by_three_for_backstage_passes_with_5_days_or_less_left():
    gilded_rose = GildedRose(
        [
            Item("Backstage passes to a TAFKAL80ETC concert", 5, 15),
        ]
    )
    expected = {"sell_in": 4, "quality": 18}

    gilded_rose.update_quality()

    item = gilded_rose.items[0]
    assert item.quality == expected["quality"]
    assert item.sell_in == expected["sell_in"]


def test_quality_decrease_twice_as_fast_after_sell_by():
    gilded_rose = GildedRose(
        [Item("+5 Dexterity Vest", 0, 20), Item("Conjured Mana Cake", 0, 6)]
    )
    expected = [
        {"sell_in": -1, "quality": 18},
        {"sell_in": -1, "quality": 2},
    ]

    gilded_rose.update_quality()

    for index, expectation in enumerate(expected):
        item = gilded_rose.items[index]
        assert item.quality == expectation["quality"]
        assert item.sell_in == expectation["sell_in"]


def test_backstage_passes_goes_to_quality_zero_after_sell_by():
    gilded_rose = GildedRose(
        [
            Item("Backstage passes to a TAFKAL80ETC concert", 0, 20),
        ]
    )
    expected = {"sell_in": -1, "quality": 0}

    gilded_rose.update_quality()

    item = gilded_rose.items[0]
    assert item.quality == expected["quality"]
    assert item.sell_in == expected["sell_in"]


def test_sulfuras_the_immutable():
    gilded_rose = GildedRose([Item("Sulfuras, Hand of Ragnaros", 0, 80)])
    expected = {"sell_in": 0, "quality": 80}

    gilded_rose.update_quality()

    item = gilded_rose.items[0]
    assert item.quality == expected["quality"]
    assert item.sell_in == expected["sell_in"]


def test_quality_does_not_increase_past_50():
    gilded_rose = GildedRose([Item("Aged Brie", 4, 49)])

    expected = {"sell_in": 3, "quality": 50}

    gilded_rose.update_quality()
    item = gilded_rose.items[0]
    assert item.quality == expected["quality"]
    assert item.sell_in == expected["sell_in"]

    expected = {"sell_in": 2, "quality": 50}

    gilded_rose.update_quality()
    item = gilded_rose.items[0]
    assert item.quality == expected["quality"]
    assert item.sell_in == expected["sell_in"]


# @pytest.mark.skip(reason="new feature")
def test_conjured_items_decrease_in_quality_twice_as_fast():
    gilded_rose = GildedRose([Item("Conjured Mana Cake", 3, 6)])
    expected = {"sell_in": 2, "quality": 4}

    gilded_rose.update_quality()

    item = gilded_rose.items[0]
    assert item.quality == expected["quality"]
    assert item.sell_in == expected["sell_in"]
