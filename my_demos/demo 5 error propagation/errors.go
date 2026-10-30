package error_demo
import "fmt"

//----------------------------

func Div(a, b int) (int) {
    return a / b
}

//-----------------------------

func div(a, b int) int {
    return a / b
}

func recoverToErr(err *error) {
    if r := recover(); r != nil {
        *err = fmt.Errorf("%v", r)
    }
}

func Div2(a, b int) (res int, err error) {
    defer recoverToErr(&err)
    return div(a, b), nil
}