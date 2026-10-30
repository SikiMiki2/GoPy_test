package small_things

type Counter struct{ N int }
func (c *Counter) Inc() { c.N++ }

func Twice(f func(int) int, x int) int { return f(f(x)) }