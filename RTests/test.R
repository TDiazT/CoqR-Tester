{if (is.list(input))
    do.call(f, c(input, list(na.rm = na.rm)))
else f(input, na.rm = na.rm)
}