"use strict";

const { add, subtract, multiply, divide } = require("../src/calculator");

describe("add", () => {
  test("adds two positive numbers", () => expect(add(2, 3)).toBe(5));
  test("adds negative numbers", () => expect(add(-1, 1)).toBe(0));
});

describe("subtract", () => {
  test("subtracts two numbers", () => expect(subtract(5, 3)).toBe(2));
});

describe("multiply", () => {
  test("multiplies two numbers", () => expect(multiply(3, 4)).toBe(12));
  test("multiply by zero", () => expect(multiply(5, 0)).toBe(0));
});

describe("divide", () => {
  test("divides two numbers", () => expect(divide(10, 2)).toBe(5));
  test("throws on divide by zero", () => {
    expect(() => divide(10, 0)).toThrow("Cannot divide by zero");
  });
});
