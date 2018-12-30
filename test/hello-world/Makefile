.DEFAULT_GOAL := all

TARGET = hello

OBJECTS = hello.o


%.o: %.c
	$(CC) -c -o $@ $< $(CFLAGS)

${TARGET}-${DOMAIN}: $(OBJECTS)
	$(LD) -o $@ $^ $(CFLAGS)


.PHONY: install clean


all: ${TARGET}-${DOMAIN}

clean:
	$(RM) ${TARGET}-${DOMAIN} ${OBJECTS}
	$(RM) ${BIN_DIR}/${TARGET}

install:
	install ${TARGET}-${DOMAIN} ${BIN_DIR}/${TARGET}