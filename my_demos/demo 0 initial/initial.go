package initial

import "strings"

func Hello(name string) string { return "Hello, " + name }

func Shout(s string) string { return strings.ToUpper(s) + "!" }

type Counter struct{ N int }

func (c *Counter) Inc() { c.N++ }

func Fib(n int) int {
    if n < 2 { return n }
    return Fib(n-1) + Fib(n-2)
}