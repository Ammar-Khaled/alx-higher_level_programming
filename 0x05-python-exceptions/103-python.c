#include <stdio.h>
#include <Python.h>

/**
 * print_python_float - prints info about python float
 */
void print_python_float(PyObject *p)
{
    double value;
    char *string_value;

    setbuf(stdout, NULL);
    printf("[.] float object info\n");

    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        setbuf(stdout, NULL);
        return;
    }

    value = ((PyFloatObject *)p)->ob_fval;

    string_value = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);
    // val=value: the value to be converted
    // format_code='r': uses the shortest representation possible.
    // precision=0: will not display any digits after the decimal point.
    // flags=Py_DTSF_ADD_DOT_0: will always add a decimal point to the string,
    // even if the value of the floating-point number is an integer.
    // type=Py_DTST_FINITE:  will only return a string
    // if the value of the floating-point number is finite.
    printf("  value: %s\n", string_value);
    setbuf(stdout, NULL);
}

/**
 * print_python_bytes - prints bytes info
 * @p: pointer to python object
 */
void print_python_bytes(PyObject *p)
{
    long int size, max_printed, i;
    char *str;

    setbuf(stdout, NULL);
    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        setbuf(stdout, NULL);
        return;
    }

    size = ((PyVarObject *)p)->ob_size;
    printf("  size: %ld\n", size);

    str = ((PyBytesObject *)p)->ob_sval;
    printf("  trying string: %s\n", str);

    if (size >= 10)
    {
        max_printed = 10;
    }
    else
    {
        max_printed = size + 1;
    }

    printf("  first %ld bytes:", max_printed);

    for (i = 0; i < max_printed; i++)
    {
        if (str[i] >= 0)
        {
            printf(" %02x", str[i]);
        }
        else
        {
            printf(" %02x", str[i] + 256);
        }
    }
    printf("\n");
    setbuf(stdout, NULL);
}

/**
 * print_python_list - print list info
 * @p: pointer to python object
 */
void print_python_list(PyObject *p)
{
    long int size, i;
    PyListObject *list;
    PyObject *item;

    setbuf(stdout, NULL);
    printf("[*] Python list info\n");

    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        setbuf(stdout, NULL);
        return;
    }

    size = ((PyVarObject *)p)->ob_size;
    printf("[*] Size of the Python List = %ld\n", size);

    list = (PyListObject *)p;
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; i++)
    {
        item = list->ob_item[i];
        printf("Element %ld: %s\n", i, (item->ob_type)->tp_name);
        if (PyBytes_Check(item))
        {
            print_python_bytes(item);
        }
        if (PyFloat_Check(item))
        {
            print_python_float(item);
        }
    }
    setbuf(stdout, NULL);
}
