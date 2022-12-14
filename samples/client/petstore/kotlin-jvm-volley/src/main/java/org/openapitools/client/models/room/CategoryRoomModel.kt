/**
 *
 * Please note:
 * This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * Do not edit this file manually.
 *
 */

@file:Suppress(
    "ArrayInDataClass",
    "EnumEntryName",
    "RemoveRedundantQualifierName",
    "UnusedImport"
)

package org.openapitools.client.models.room

import androidx.room.Entity
import androidx.room.Ignore
import androidx.room.PrimaryKey
import org.openapitools.client.models.*


@Entity(tableName = "Category")
/**
* Room model for A category for a pet
* @param id 
* @param name 
*/
data class CategoryRoomModel (
    @PrimaryKey(autoGenerate = true) var roomTableId: Int,
    
    var id: kotlin.Long? = null,
    var name: kotlin.String? = null,
    
    ) {

    companion object { }

        fun toApiModel(): Category = Category(
        id = this.id,
        name = this.name,
        )
}
