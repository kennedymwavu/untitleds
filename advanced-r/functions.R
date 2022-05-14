# Quiz:
# 1:
x <- 10

f1 <- function(x) {
  function() {
    x + 10
  }
}

f1(1)()

# 2:
`+`(1, `*`(2, 3))

1 + 2 * 3

sum(1, prod(2, 3))

# 3:
mean(, TRUE, x = c(1:10, NA))
# Idk this

# 4:
f2 <- function(a, b) {
  a * 10
}

f2(10, stop("This is an error!"))


# Infix fn:
`%+%` <- function(a, b) a + b
1 %+% 1

# Replacement fn:
# ?


body(body)

f <- function(x) x ** 5

body(f)

body(f) <- quote(5 ** x)
f
f(2)

body(f) <- 2 * 5
f

body(f) <- y * 2

s <- expression(a + b)
substitute(eval(quote(s)), list(a = 1))
substitute(expression(a + b), list(a = 1))
