<?xml version="1.0" encoding="UTF-8" ?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
	<xsl:template match="/order">
		<code>
            <xsl:apply-templates select="item"/> 
        </code>
	</xsl:template>
	<xsl:template match="item">
		name: <xsl:value-of select="name" />,
		quantity: <xsl:value-of select="quantity" />;
	</xsl:template>
</xsl:stylesheet>
