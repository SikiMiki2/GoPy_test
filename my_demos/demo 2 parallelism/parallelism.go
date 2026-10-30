package fast

import "sync"

func isPrime(n int) bool {
    if n < 2 { return false }
    for i := 2; i*i <= n; i++ {
        if n%i == 0 { return false }
    }
    return true
}

func CountPrimes(limit, workers int) int {
    var wg sync.WaitGroup
    counts := make([]int, workers)
    for w := 0; w < workers; w++ {
        wg.Add(1)
        go func(w int) {
            defer wg.Done()
            c := 0
            for n := w; n < limit; n += workers {
                if isPrime(n) { c++ }
            }
            counts[w] = c
        }(w)
    }
    wg.Wait()
    total := 0
    for _, c := range counts { total += c }
    return total
}