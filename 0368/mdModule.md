---
title: "Module 0368: Tracking changes of a circuit"
author: Tak Auyeung
---

* Terms:
  * Port: a port is a point of connection on a component, such as a gate, to a wire.
  * Node: a node is a collection of wires that are electrically connected.
  * Component: a component is typically a gate or a device that has input ports and output ports.
  * Propagational delay: it takes a short amount of time for a component to update its output port(s) after at least one of the input ports is changed. This amount of time is called a propagational delay.

In pseudocode, the logic can be summarized as follows:

* Begin with a starting state. This is usually signified by **NC** boldfaced.
  * The initial changes to the input pins are usually **boldfaced** on this row.
  * For the initial NC row, update ports node-connected to the ports of updated input pins.
* Perform the following steps until there is no change from the last step (PD row):
  * This is an NC (node connectivity) row. Depending on the *wiring* of the circuit, update all other ports of the same node connected to a port that is changed.
    * As a general rule, an NC row should only have ports corresponding to input pins changed. The port of an output pin is considered an input.
  * This is a PD (propagational delay) row. After a propagational delay, analyze and compute the output port(s) of every component with at least one input port changed in the previous NC step.
    * Only record in the table if an output port is changed from its current value.
    * As a general rule, a PD row should only have ports corresponding to the changed output pins.
    * When a PD row is empty, reflecting there is no change, then a steady state is reached.

Mechanically, this can be done by using a spreadsheet or any table.
