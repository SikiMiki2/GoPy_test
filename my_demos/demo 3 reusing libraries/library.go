package libraries_in_go

import "github.com/dustin/go-humanize"

func Size(n int) string { return humanize.Bytes(uint64(n)) }