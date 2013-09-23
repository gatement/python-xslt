from lxml import etree
import StringIO 

#xslt_root = etree.XML('''\
#<xsl:stylesheet version="1.0"
#xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
#    <xsl:template match="/">
#        <foo><xsl:value-of select="/a/b/text()" /></foo>
#    </xsl:template>
#</xsl:stylesheet>''')
xslt_root = etree.parse("./test.xsl");
#print etree.tostring(xslt_root.getroot(), pretty_print=True)
transform = etree.XSLT(xslt_root)

#f = StringIO.StringIO('<a><b>Text</b></a>')
#doc = etree.parse(f)
doc = etree.parse("./test.xml")
#print etree.tostring(doc.getroot(), pretty_print=True)

result_tree = transform(doc)
print result_tree.getroot().text
#result = etree.tostring(result_tree.getroot(), pretty_print=True)
#print result

with open("./code.java", "w") as output_file:
    output_file.write(result_tree.getroot().text)
