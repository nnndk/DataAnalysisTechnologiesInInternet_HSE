<?xml version="1.0" encoding="utf-8"?>
<!--https://magictool.ai/tool/xslt-transformation/-->
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:output method="text" indent="yes"/>

	<xsl:template match="/">
		<xsl:text>Timetable&#xa;</xsl:text>

		<xsl:for-each select="timetable/day">
			<xsl:value-of select="@name"/>
			<xsl:text>&#xa;</xsl:text>

			<xsl:for-each select="./class">
				<xsl:text>&#9;Start:&#160;</xsl:text>
				<xsl:value-of select="@startTime"/>
				<xsl:text>&#xa;</xsl:text>

				<xsl:text>&#9;End:&#160;</xsl:text>
				<xsl:value-of select="@endTime"/>
				<xsl:text>&#xa;</xsl:text>

				<xsl:text>&#9;Title:&#160;</xsl:text>
				<xsl:value-of select="title"/>
				<xsl:text>&#xa;</xsl:text>

				<xsl:text>&#9;Teacher:&#160;</xsl:text>
				<xsl:value-of select="teacher"/>
				<xsl:text>&#xa;</xsl:text>

				<xsl:text>&#9;Type:&#160;</xsl:text>
				<xsl:value-of select="@type"/>
				<xsl:text>&#xa;</xsl:text>

				<xsl:text>&#9;Room:&#160;</xsl:text>
				<xsl:value-of select="room/roomNumber"/>[<xsl:value-of select="room/buildingNumber"/>]
				<xsl:text>&#xa;</xsl:text>
			</xsl:for-each>
			<xsl:text>&#xa;</xsl:text>
		</xsl:for-each>
	</xsl:template>

</xsl:stylesheet>