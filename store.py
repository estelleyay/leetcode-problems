"""Assignment 1 - Grocery Store Models (Task 1)

CSC148 Winter 2024
Department of Computer Science,
University of Toronto

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

All of the files in this directory are
Copyright (c) Jonathan Calver, Diane Horton, Sophia Huynh, Joonho Kim and
Jacqueline Smith.

Module Description:

This file contains all the classes necessary to model the relevant entities
in a grocery store.
"""
from __future__ import annotations
from typing import TextIO
import json

# The maximum number of items a customer can have if they use an express line.
EXPRESS_LIMIT = 7


class NoAvailableLineError(Exception):
    """Represents a situation in which a customer has arrived at the checkout
    area and there is no line available for them to join.
    """

    def __str__(self) -> str:
        return 'No line available'


class GroceryStore:
    """A grocery store.

    A grocery store consists of checkout lines.

    TODO: Add one or more attributes to store the checkout lines.
        Include documentation, a type contract, and appropriate Representation
        Invariants for any attribute(s) you add.

    Attributes:
    - num_lines: How many lines this grocery store has.

    Representation Invariants:
    - self.num_lines > 0
    """
    num_lines: int

    def __init__(self, config_file: TextIO) -> None:
        """Initialize a GroceryStore from a configuration file <config_file>.

        Preconditions:
        - config_file is a valid JSON configuration file with the keys
          regular_count, express_count, self_serve_count, and line_capacity
        - config_file is open
        - All values in config_file are >= 0
        """
        # TODO: Implement this method

    def enter_line(self, customer: Customer) -> int:
        """Pick a new line for <customer> to join, using the algorithm from
        the handout and add <customer> to that line.

        Return the index of the line that the customer joined.

        Raise a NoAvailableLineError if there is no line available for the
        customer to join.

        Preconditions:
        - customer is not currently in any line in this GroceryStore
        """
        # TODO: Implement this method

    def next_checkout_time(self, line_number: int) -> int:
        """Return the time it will take to check out the customer at the front
        of line <line_number>.

        Preconditions:
        - 0 <= line_number < self.num_lines
        """
        # TODO: Implement this method

    def remove_front_customer(self, line_number: int) -> int:
        """If there is any customer (or customers) in checkout line
        <line_number>, remove the front customer.

        Return the number of customers remaining in line <line_number>.

        Preconditions:
        - 0 <= line_number < self.num_lines
        """
        # TODO: Implement this method

    def close_line(self, line_number: int) -> list[Customer]:
        """Close checkout line <line_number> by updating its status to indicate
        that it is closed and removing from it all customers after the first
        one.

        Return a new list with these removed customers, in the same order as
        they appeared in the line before it closed.

        Preconditions:
        - 0 <= line_number < self.num_lines
        """
        # TODO: Implement this method

    def first_in_line(self, line_number: int) -> Customer | None:
        """Return the first customer in line <line_number>, or None if there
        are no customers in line.

        Do not change the line, however.

        Preconditions:
        - 0 <= line_number < self.num_lines
        """
        # TODO: Implement this method


class Customer:
    """A grocery store customer.

    Attributes:
    - name: A unique identifier for this customer.
    - arrival_time: The first time this customer arrived at the checkout area
      and attempted to join a line, or None if they have not yet arrived.
    - _items: The items this customer has.

    Representation Invariants:
    - self.arrival_time is None or self.arrival_time >= 0
    """
    name: str
    arrival_time: int | None
    _items: list[Item]

    def __init__(self, name: str, items: list[Item]) -> None:
        """Initialize a customer with the given <name> and a copy of the
        list <items>.

        The customer's arrival_time is initially None.

        >>> item_list = [Item('bananas', 7)]
        >>> belinda = Customer('Belinda', item_list)
        >>> belinda.name
        'Belinda'
        >>> belinda._items == item_list
        True
        >>> belinda._items is item_list
        False
        >>> belinda.arrival_time is None
        True
        """
        # TODO: Implement this method

    def num_items(self) -> int:
        """Return the number of items this customer has.

        >>> c = Customer('Bo', [Item('bananas', 7), Item('cheese', 3)])
        >>> c.num_items()
        2
        """
        # TODO: Implement this method

    def item_time(self) -> int:
        """Return the number of seconds it takes for a cashier to check out
        this customer, that is, the time it takes to check out this customer
        at a regular or express line.

        >>> c = Customer('Bo', [Item('bananas', 7), Item('cheese', 3)])
        >>> c.item_time()
        10
        """
        # TODO: Implement this method


class Item:
    """An item to be checked out.

    Attributes:
    - name: the name of this item
    - time: the amount of time it takes a cashier to check out this item

    Representation Invariants:
    - self.time > 0
    """
    name: str
    time: int

    def __init__(self, name: str, time: int) -> None:
        """Initialize a new item with <name> and <time>.

        Preconditions:
        - time > 0

        >>> item = Item('bananas', 7)
        >>> item.name
        'bananas'
        >>> item.time
        7
        """
        self.name = name
        self.time = time


class CheckoutLine:
    """A checkout line in a grocery store.

    This is an abstract class and should not be instantiated.

    Attributes:
    - capacity: The maximum number of customers allowed in this CheckoutLine.
    - is_open: True iff the line is open.
    - _queue: Customers in this line in order by arrival time, with the
                earliest arrival at the front of the list.

    Representation Invariants:
    - len(self) <= self.capacity
    - capacity > 0
    """
    capacity: int
    is_open: bool
    _queue: list[Customer]

    def __init__(self, capacity: int) -> None:
        """Initialize an open and empty CheckoutLine, with the given <capacity>.

        Preconditions:
        - capacity > 0

        >>> line = CheckoutLine(1)
        >>> line.capacity
        1
        >>> line.is_open
        True
        >>> line._queue
        []
        """
        # TODO: Implement this method

    def __len__(self) -> int:
        """Return the length of this CheckoutLine.

        >>> line = CheckoutLine(10)
        >>> len(line)
        0
        """
        # TODO: Implement this method

    def can_accept(self, customer: Customer) -> bool:
        """Return True iff this CheckoutLine can accept <customer>.

        >>> line = CheckoutLine(1)
        >>> line.can_accept(Customer('Sophia', []))
        True
        """
        # TODO: Implement this method

    def accept(self, customer: Customer) -> bool:
        """Accept <customer> into the end of this CheckoutLine if possible.

        Return True iff the customer is accepted.

        >>> line = CheckoutLine(1)
        >>> c1 = Customer('Belinda', [Item('cheese', 3)])
        >>> c2 = Customer('Hamman', [Item('chips', 4), Item('gum', 1)])
        >>> line.accept(c1)
        True
        >>> line.accept(c2)
        False
        >>> len(line)
        1
        >>> line.first_in_line() is c1
        True
        """
        # TODO: Implement this method

    def next_checkout_time(self) -> int:
        """Return the time it will take to check out the customer at the front
        of this line.

        Preconditions:
        - self.first_in_line() is not None

        No doctests provided, since this method is abstract.
        """
        raise NotImplementedError

    def remove_front_customer(self) -> int:
        """If there is any customer (or customers) in this checkout line,
        remove the front customer.

        Return the number of customers remaining in the line.

        >>> line = CheckoutLine(1)
        >>> line.accept(Customer('Sophia', [Item('red snapper', 21)]))
        True
        >>> line.remove_front_customer() # No one is left in line.
        0
        >>> line.remove_front_customer() # It's still okay to call the method.
        0
        """
        # TODO: Implement this method

    def close(self) -> list[Customer]:
        """Close this line by updating its status to indicate that it is closed
        and removing from it all customers after the first one.

        Return a new list with these removed customers, in the same order as
        they appeared in the line before it closed.

        >>> line = CheckoutLine(2)
        >>> line.close()
        []
        >>> line.is_open
        False
        """
        # TODO: Implement this method

    def first_in_line(self) -> Customer | None:
        """Return the first customer in this line, or None if there are no
        customers in line.

        Do not change the line, however.

        >>> line = CheckoutLine(1)
        >>> line.first_in_line() is None
        True
        """
        # TODO: Implement this method


# TODO: create subclasses for the different types of events below.
class RegularLine(CheckoutLine):
    """A regular CheckoutLine.
    """
    # TODO: Implement this class


class ExpressLine(CheckoutLine):
    """An express CheckoutLine.
    """
    # TODO: Implement this class


class SelfServeLine(CheckoutLine):
    """A self-serve CheckoutLine.
    """
    # TODO: Implement this class


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    check_pyta = True
    if check_pyta:
        import python_ta

        python_ta.check_all(config={
            'allowed-import-modules': ['__future__', 'typing', 'json',
                                       'python_ta', 'doctest'],
            'disable': ['W0613']})
