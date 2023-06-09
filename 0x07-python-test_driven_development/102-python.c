#include <stdio.h>
#include <string.h>
#include <Python.h>

/**
 * print_python_string - prints python string object information
 * @p: pointer to the python object
 */
void print_python_string(PyObject *p)
{
    char *str;

    printf("[.] string object info\n");

    /*checks if the PyObject represents a string object*/
    if (strcmp("str", p->ob_type->tp_name) != 0)
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    if (PyUnicode_IS_COMPACT_ASCII(p))
    {
        printf("  type: compact ascii\n");
    }
    else
    {
        printf("  type: compact unicode object\n");
    }

    printf("  length: %ld\n", PyUnicode_GET_SIZE(p));

    str = PyUnicode_AsEncodedString(p, "utf-8","~E~");
    /**
     * this function converts unicode string object to a bytes object
     * p: the Unicode string object to be encoded.
     * utf-8: the encoding to use for the conversion.
     * "~E~": is an error handling parameter
     * that specifies how to handle errors during the encoding process.
     * "~E~" value indicates that encoding errors should be replaced with
     *  the "Unicode replacement character" <?> (65533),
     *  which is a special character indicates that a character
     *  could not be represented in the target encoding.
     */

    printf("  value: %s\n", PyBytes_AsString(str));
}
